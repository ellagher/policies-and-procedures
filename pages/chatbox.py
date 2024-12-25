import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
import uuid

from chat_llm_main import initialize_graph, run_graph_with_query

graph = initialize_graph()

def create_user_bubble(user_text):
    """Creates a chat bubble for the user's message."""
    return html.Div(
        user_text,
        style={
            "backgroundColor": "#555555",
            "borderRadius": "15px",
            "padding": "10px",
            "margin": "5px 0",
            "textAlign": "right",
            "maxWidth": "70%",
            "alignSelf": "flex-end",
            "boxShadow": "0px 2px 8px rgba(0, 0, 0, 0.4)",
            "wordWrap": "break-word",
            "fontSize": "14px",
            "color": "#f0f0f0",
        },
    )

def create_nancy_loading_bubble():
    """Show Nancy's icon and a simple gray 'Nancy is typing...' text."""
    return html.Div(
        [
            html.Img(
                src="/assets/nancy.png",
                style={
                    "width": "30px",
                    "height": "30px",
                    "marginRight": "5px",
                    "borderRadius": "50%",
                    "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.3)",
                },
            ),
            html.Div(
                "Nancy is typing...",
                style={
                    "fontSize": "14px",
                    "color": "#a9a9a9",
                    "margin": "0",
                },
            ),
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "margin": "5px 0",
        },
    )
def create_nancy_response_bubble(response_text):
    """Assistant message with Nancy's logo to the left and Markdown support for the text."""
    return html.Div(
        [
            html.Img(
                src="/assets/nancy.png",
                style={
                    "width": "30px",
                    "height": "30px",
                    "marginRight": "10px",  
                    "borderRadius": "50%",  
                    "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",  
                },
            ),
            dcc.Markdown(
                response_text,
                style={
                    "color": "#333333",
                    "fontSize": "14px",
                    "lineHeight": "1.5",
                    "maxWidth": "85%",
                    "wordWrap": "break-word",
                },
            ),
        ],
        style={
            "display": "flex",
            "alignItems": "flex-start",
            "margin": "10px 0",
        },
    )

def chatbox_layout():
    return html.Div(
        [
            html.Div(
                id="chat-window",
                style={
                    "flex": 1,
                    "overflowY": "auto",
                    "padding": "15px",
                    "backgroundColor": "#ffffff",
                    "display": "flex",
                    "flexDirection": "column",
                    "scrollbarWidth": "none",  
                    "-ms-overflow-style": "none",
                },
            ),
            dbc.InputGroup(
                [
                    dbc.Input(
                        id="chat-input",
                        placeholder="Type your message here...",
                        type="text",
                        style={
                            "borderRadius": "15px 0 0 15px",
                            "padding": "15px",
                            "fontSize": "14px",
                            "backgroundColor": "#ffffff",
                            "color": "#333333",
                            "flex": "1",
                            "border": "none",
                            "outline": "none",
                            "boxShadow": "none",
                        },
                    ),
                    html.Button(
                        html.Img(
                            src="/assets/send-icon.png",
                            style={
                                "width": "25px",
                                "height": "25px",
                                "cursor": "pointer",
                            },
                        ),
                        id="send-button",
                        disabled=True,
                        style={
                            "background": "none",
                            "border": "none",
                            "width": "45px",
                            "height": "45px",
                            "padding": "10px",
                            "margin": "0",
                            "borderRadius": "0 15px 15px 0",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "cursor": "pointer",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "borderRadius": "0 0 15px 15px",
                    "boxShadow": "0px -1px 5px rgba(0, 0, 0, 0.1)",
                    "backgroundColor": "#ffffff",
                    "overflow": "hidden",
                    "flexShrink": 0,
                },
            ),
            dcc.Store(id="session-id", storage_type="session"),
            dcc.Store(id="chat-store", storage_type="session"),
            dcc.Store(id="trigger-llm", data=False, storage_type="memory"),
        ],
        style={
            "position": "fixed",
            "top": "36px",
            "right": "0",
            "width": "50%",
            "bottom": "20px",
            "display": "flex",
            "flexDirection": "column",
            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
            "backgroundColor": "#ffffff",
            "borderRadius": "15px",
            "overflow": "hidden",
        },
    )

@callback(
    Output("session-id", "data"),
    Input("url", "pathname"),  
)
def generate_session_id(pathname):
    return str(uuid.uuid4())

@callback(
    Output("chat-store", "data"),
    Input("session-id", "data"),
    prevent_initial_call=True
)
# def clear_chatstore_on_new_session(_new_session_id):
#     return []

def clear_chatstore_on_new_session(_new_session_id):
    return [
        {
            "type": "nancy_response",
            "content": "Hi there! I'm Nancy, your assistant. How can I help you today?"
        }
    ]

@callback(
    Output("chat-window", "children"),
    Input("chat-store", "data"),
    prevent_initial_call=False  
)
def render_chat_window(chat_data):
    """
    Render chat bubbles from the chat-store data.
    """
    chat_window_children = []
    for entry in chat_data:
        if entry["type"] == "user":
            chat_window_children.append(create_user_bubble(entry["content"]))
        elif entry["type"] == "nancy_response":
            chat_window_children.append(create_nancy_response_bubble(entry["content"]))
        elif entry["type"] == "nancy_loading":
            chat_window_children.append(create_nancy_loading_bubble())
    return chat_window_children

@callback(
    Output("send-button", "disabled"),
    Input("chat-input", "value")
)
def toggle_send_button_disable(input_value):
    """
    If there's no text, disable the button => True.
    Otherwise, enable => False.
    """
    if not input_value or not input_value.strip():
        return True
    return False


@callback(
    Output("chat-store", "data", allow_duplicate=True),
    Output("chat-window", "children", allow_duplicate=True),
    Output("chat-input", "value"),  
    Output("trigger-llm", "data", allow_duplicate=True),
    Input("send-button", "n_clicks"),
    Input("chat-input", "n_submit"),
    State("chat-input", "value"),
    State("chat-store", "data"),
    prevent_initial_call=True
)
def user_message_and_loading(n_clicks, n_submit, user_message, chat_data):
    if not chat_data:
        chat_data = []

    if not user_message:
        return chat_data, [], "", False

    chat_data.append({
        "type": "user",
        "content": user_message
    })

    loading_indicator_id = str(uuid.uuid4())  
    chat_data.append({
        "type": "nancy_loading",
        "content": "Nancy is typing...",
        "id": loading_indicator_id,
    })

    chat_window_children = []
    for entry in chat_data:
        if entry["type"] == "user":
            chat_window_children.append(create_user_bubble(entry["content"]))
        elif entry["type"] == "nancy_response":
            chat_window_children.append(create_nancy_response_bubble(entry["content"]))
        elif entry["type"] == "nancy_loading":
            chat_window_children.append(create_nancy_loading_bubble())

    return chat_data, chat_window_children, "", True

@callback(
    Output("chat-store", "data", allow_duplicate=True),
    Output("chat-window", "children", allow_duplicate=True),
    Output("trigger-llm", "data", allow_duplicate=True),
    Input("trigger-llm", "data"),
    State("chat-store", "data"),
    State("session-id", "data"),
    prevent_initial_call=True
)
def replace_loading_with_llm_response(trigger, chat_data, session_id):
    if not trigger or not chat_data:
        return chat_data, [], False

    loading_index = None
    for i in reversed(range(len(chat_data))):
        if chat_data[i]["type"] == "nancy_loading":
            loading_index = i
            break

    if loading_index is None:
        return chat_data, [], False

    user_question = None
    for i in reversed(range(loading_index)):
        if chat_data[i]["type"] == "user":
            user_question = chat_data[i]["content"]
            break

    if not user_question:
        return chat_data, [], False

    try:
        assistant_response = run_graph_with_query(graph, user_question, session_id)
    except Exception as e:
        assistant_response = f"An error occurred: {str(e)}"

    chat_data[loading_index] = {
        "type": "nancy_response",
        "content": assistant_response
    }

    chat_window_children = []
    for entry in chat_data:
        if entry["type"] == "user":
            chat_window_children.append(create_user_bubble(entry["content"]))
        elif entry["type"] == "nancy_response":
            chat_window_children.append(create_nancy_response_bubble(entry["content"]))
        elif entry["type"] == "nancy_loading":
            chat_window_children.append(create_nancy_loading_bubble())

    return chat_data, chat_window_children, False
