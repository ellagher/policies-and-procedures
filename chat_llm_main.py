import os
import time
import uuid
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import PineconeVectorStore
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool
from langgraph.graph import MessagesState, StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages.ai import AIMessage
from pinecone import Pinecone, ServerlessSpec

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

def initialize_llm():
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0.3,
        openai_api_key=OPENAI_API_KEY
    )

class PineconeInitializer:
    def __init__(self, index_name: str, dimension: int = 3072):
        self.index_name = index_name
        self.dimension = dimension
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not self.pinecone_api_key:
            raise ValueError("PINECONE_API_KEY not found in environment variables.")

    def initialize_pinecone(self):
        pc = Pinecone(api_key=self.pinecone_api_key)
        existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

        if self.index_name not in existing_indexes:
            pc.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            while not pc.describe_index(self.index_name).status["ready"]:
                time.sleep(1)

        index = pc.Index(self.index_name)
        return index


def load_and_vectorize_data(folder_path: str = "data/", chunk_size=1000, chunk_overlap=250):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            loader = PyPDFLoader(pdf_path)
            pdf_docs = loader.load()
        
            # Add the filename to each document's metadata
            for doc in pdf_docs:
                doc.metadata["file_name"] = filename
                doc.page_content = f"Filename: {filename}\n{doc.page_content}"
            
            documents.extend(pdf_docs)
            #documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    splits = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=OPENAI_API_KEY)

    pinecone_initializer = PineconeInitializer(index_name="rag-csv-index")
    pinecone_index = pinecone_initializer.initialize_pinecone()

    uuids = [str(uuid.uuid4()) for _ in range(len(splits))]
    global vector_store
    vector_store = PineconeVectorStore(index=pinecone_index, embedding=embeddings)
    vector_store.add_documents(documents=splits, ids=uuids)

    retriever = vector_store.as_retriever(search_kwargs={"k": 10})
    return retriever

def initialize_tool():
    retriever = load_and_vectorize_data()

    @tool(response_format="content_and_artifact")
    def retrieve(query: str):
        """Retrieve information related to a query."""
        retrieved_docs = vector_store.similarity_search(query, k=10)
        serialized = "\n\n".join(
            (f"Source: {doc.metadata}\nContent: {doc.page_content}")
            for doc in retrieved_docs
        )
        return serialized, retrieved_docs
    
    return retrieve

persistent_memory = MemorySaver() 

def build_graph_with_memory(llm, retrieve_tool, memory=persistent_memory):
    def query_or_respond(state: MessagesState):
        llm_with_tools = llm.bind_tools([retrieve_tool])
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    def generate(state: MessagesState):
        recent_tool_messages = []
        for message in reversed(state["messages"]):
            if message.type == "tool":
                recent_tool_messages.append(message)
            else:
                break
        tool_messages = recent_tool_messages[::-1]

        docs_content = "\n\n".join(doc.content for doc in tool_messages)

        system_message_content = (
            "You are Nancy, an assistant for answering questions about policies and procedures. "
            "Retrieve and use information solely from the relevant provided documents to respond to the user's query. "
            "You can summarize a document if requested, or answer specific questions. "
            "For summarization tasks, provide a detailed summary by extracting and presenting all key points, themes, and significant details from the entire document. "
            "Ensure the summary captures the essence of each section and includes specific information where relevant. "
            "Explicitly include the source document's title and the page number(s) used to generate the response. "
            "If no relevant information is found in the documents, clearly state, 'I do not have information about this in the provided documents.' "
            "For detailed summaries, organize the content logically and ensure completeness to provide an accurate understanding of the document.\n\n"
            f"{docs_content}"
        )


        conversation_messages = [
            message
            for message in state["messages"]
            if message.type in ("human", "system") or (message.type == "ai" and not message.tool_calls)
        ]
        prompt = [SystemMessage(system_message_content)] + conversation_messages
        response = llm.invoke(prompt)
        return {"messages": [response]}

    graph_builder = StateGraph(MessagesState)
    graph_builder.add_node(query_or_respond)
    graph_builder.add_node(ToolNode([retrieve_tool]))
    graph_builder.add_node(generate)

    graph_builder.set_entry_point("query_or_respond")

    graph_builder.add_conditional_edges(
        "query_or_respond",
        tools_condition,
        {END: END, "tools": "tools"},
    )
    graph_builder.add_edge("tools", "generate")
    graph_builder.add_edge("generate", END)

    return graph_builder.compile(checkpointer=memory)

def initialize_graph():
    llm = initialize_llm()
    retrieve_tool = initialize_tool()

    return build_graph_with_memory(llm, retrieve_tool)




def run_graph_with_query(graph, question, session_id):
    """Run the graph with a given question and session ID."""

    state = {"messages": [{"role": "user", "content": question}]}
    config = {"configurable": {"thread_id": session_id}}
    responses = []
    logger.info(f"Initial State: {state}")
    logger.info(f"Config: {config}")

    # for step in graph.stream(state, stream_mode="values", config=config):
    #     responses.append(step["messages"][-1])

    for step in graph.stream(state, stream_mode="values", config=config):
        #logger.info(f"Step Output: {step}")
        state["messages"].append(step["messages"][-1])
        responses.append(step["messages"][-1])
        #logger.info(f"Updated State: {state}")


    logger.info(f"Final Responses: {responses}")

    # ai_message_content = next((msg.content for msg in responses if isinstance(msg, AIMessage)), None)
    ai_message_content = next(
    (msg.content for msg in responses if isinstance(msg, AIMessage) and msg.content.strip()),
    None
)

    logger.info(f"this is the ai message: {ai_message_content}")
    
    if ai_message_content is None:
        raise ValueError("Please ask your question again.")
    
    return ai_message_content
