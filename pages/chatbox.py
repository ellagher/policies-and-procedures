import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
from chat_llm_main import initialize_graph, run_graph_with_query
import uuid

graph = initialize_graph()

def chatbox_layout():
    return html.Div(
        [
            html.Div(
                id="chat-window",
                style={
                    "border": "1px solid #ddd",
                    "borderRadius": "15px",
                    "height": "85%",
                    "overflowY": "scroll",
                    "padding": "15px",
                    "backgroundColor": "#f7f8fa",
                    "marginBottom": "10px",
                    "display": "flex",
                    "flexDirection": "column",
                    "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                },
            ),
            dbc.InputGroup(
                [
                    dbc.Input(
                        id="chat-input",
                        placeholder="Type your message here...",
                        type="text",
                        style={
                            "borderRadius": "15px",
                            "padding": "12px",
                            "fontSize": "14px",
                            "flex": "1",
                            "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.1)",
                        },
                    ),
                    dbc.Button(
                        html.Img(
                            src="/assets/send-icon.png",  
                            style={
                                "width": "20px",
                                "height": "20px",
                            },
                        ),
                        id="send-button",
                        color="link",  
                        style={
                            "borderRadius": "50%",
                            "padding": "10px",
                            "border": "none",
                        },
                    ),
                ],
                style={"display": "flex", "alignItems": "center"},
            ),
            dbc.Spinner(
                id="loading-indicator",
                color="primary",
                spinner_style={"display": "none", "margin": "10px auto"},
            ),
            dcc.Store(id="session-id", storage_type="session"),
        ],
        style={
            "position": "fixed",
            "top": "20px",
            "right": "0",
            "width": "50%",  
            "height": "calc(100% - 40px)",  
            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.15)",
            "backgroundColor": "#fff",
            "borderRadius": "15px",
            "padding": "15px",
            "overflow": "hidden",
        },
    )

@callback(
    Output("session-id", "data"),
    Input("url", "pathname"),  
)
def generate_session_id(pathname):
    return str(uuid.uuid4())  

from dash import html, dcc, callback, Input, Output, State, ctx

@callback(
    Output("chat-window", "children"),
    Output("chat-input", "value"),  
    Output("loading-indicator", "style"),  
    Input("send-button", "n_clicks"),
    Input("chat-input", "n_submit"),  
    State("chat-input", "value"),
    State("chat-window", "children"),
    State("session-id", "data"),  
    prevent_initial_call="initial_duplicate",
)
def update_chat_window(n_clicks, n_submit, user_message, chat_history, session_id):
    if not chat_history:
        chat_history = []

    if user_message:
        chat_history.append(
            html.Div(
                user_message,
                style={
                    "backgroundColor": "#e6f7ff",
                    "borderRadius": "15px",
                    "padding": "10px",
                    "margin": "5px 0",
                    "textAlign": "right",
                    "maxWidth": "70%",
                    "alignSelf": "flex-end",  
                    "boxShadow": "0px 2px 8px rgba(0, 0, 0, 0.1)",
                    "wordWrap": "break-word",  
                    "fontSize": "14px",
                    "color": "#0056b3",
                },
            )
        )

    loading_style = {"display": "block"}  

    try:
        assistant_response = run_graph_with_query(graph, user_message, session_id)
    except Exception as e:
        assistant_response = f"An error occurred: {str(e)}"

    loading_style = {"display": "none"}

    chat_history.append(
        html.Div(
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
                    assistant_response,
                    style={
                        "fontSize": "14px",
                        "color": "#333",
                        "backgroundColor": "#f1f1f1",
                        "padding": "10px",
                        "borderRadius": "15px",
                        "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.1)",
                        "maxWidth": "70%",
                        "wordWrap": "break-word",
                    },
                ),
            ],
            style={
                "display": "flex",
                "alignItems": "center",
                "margin": "10px 0",
            },
        )
    )

    return chat_history, "", loading_style
