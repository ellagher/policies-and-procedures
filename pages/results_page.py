# import dash_bootstrap_components as dbc
# from dash import html, dcc
# import flask
# from pages.chatbox import chatbox_layout


# # Table layout for displaying search results
# results_page_layout = dbc.Container([
#     # Back and Home Buttons using dcc.Link
#     html.Div([
#         dcc.Link(
#             html.Img(
#                 src="/assets/back.png",
#                 style={
#                     "width": "30px",
#                     "height": "30px",
#                     "position": "absolute",
#                     "top": "20px",
#                     "left": "20px",
#                     "zIndex": "9999",
#                     "cursor": "pointer"
#                 }
#             ),
#             href='/'  # Navigates to the search page
#         ),
#         dcc.Link(
#             html.Img(
#                 src="/assets/home_button.png",
#                 style={
#                     "width": "33px",
#                     "height": "31px",
#                     "position": "absolute",
#                     "top": "20px",
#                     "right": "20px",
#                     "zIndex": "9999",
#                     "cursor": "pointer"
#                 }
#             ),
#             href='/'  # Navigates to the home page (search page)
#         )
#     ]),
#     dbc.Row([
#         dbc.Col(
#             [
#                 # Table with headers and rows for each document
#                 dbc.Table([
#                     html.Thead(html.Tr([
#                         html.Th("Title", style={"textAlign": "left", "width": "30%"}),
#                         html.Th("Department", style={"textAlign": "center", "width": "15%"}),
#                         html.Th("Revision Date", style={"textAlign": "center", "width": "15%"}),
#                         html.Th("Status", style={"textAlign": "center", "width": "10%"}),
#                         html.Th("Last Modified By", style={"textAlign": "center", "width": "15%"}),
#                         html.Th("Action", style={"textAlign": "center", "width": "15%"})
#                     ])),
#                     html.Tbody([
#                         html.Tr([
#                             html.Td("Fall Prevention Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Surgery"), style={"textAlign": "center"}),
#                             html.Td("2022-03-15", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jane Smith", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Targeted Temperature Management TTM Post Resuscitated Cardiac Arrest",
#                                     style={"textAlign": "left"}),
#                             html.Td(html.B("Nursing"), style={"textAlign": "center"}),
#                             html.Td("2022-05-30", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jessica Brown", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Infection Control Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Infection Control"), style={"textAlign": "center"}),
#                             html.Td("2021-11-22", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Inactive", color="danger", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("John Doe", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Medication Administration Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Nursing"), style={"textAlign": "center"}),
#                             html.Td("2022-06-10", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jill Johnson", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Wound Care Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Nursing"), style={"textAlign": "center"}),
#                             html.Td("2022-01-05", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Julia Black", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Emergency Preparedness Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Emergency"), style={"textAlign": "center"}),
#                             html.Td("2021-12-20", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Justin Blue", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Pain Management Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Orthopedic"), style={"textAlign": "center"}),
#                             html.Td("2022-04-18", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jeremy Green", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),

#                         html.Tr([
#                             html.Td("Quality Improvement Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Quality"), style={"textAlign": "center"}),
#                             html.Td("2022-02-14", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jim Davis", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/data/document.txt", style={"color": "blue"}))
#                         ]),
#                     ])
#                 ], bordered=True, striped=True, hover=True, responsive=True, style={"marginTop": "20px"})
#             ],
#             width=6  # Occupies half of the page width
#         ),
#         dbc.Col(chatbox_layout(), width=6)  # Empty column to fill the right half
#     ], justify="start"),
# ], fluid=True, style={
#     "padding": "20px",
#     "backgroundColor": "#ffffff",
#     "borderRadius": "10px",
#     "position": "relative"  # Necessary for absolute positioning of buttons
# })

# - document_page.py is no longer needed
import dash_bootstrap_components as dbc
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from pages.chatbox import chatbox_layout

def build_table_layout():
    return dbc.Table(
        [
            html.Thead(
                html.Tr([
                    html.Th("Title", style={"textAlign": "left", "width": "30%"}),
                    html.Th("Department", style={"textAlign": "center", "width": "15%"}),
                    html.Th("Revision Date", style={"textAlign": "center", "width": "15%"}),
                    html.Th("Status", style={"textAlign": "center", "width": "10%"}),
                    html.Th("Last Modified By", style={"textAlign": "center", "width": "15%"}),
                    html.Th("Action", style={"textAlign": "center", "width": "15%"}),
                ])
            ),
            html.Tbody([

                html.Tr([
                    html.Td("Urinary Catheterisation for Adults Clinical Guideline", style={"textAlign": "left"}),
                    html.Td(html.B("Surgery"), style={"textAlign": "center"}),
                    html.Td("2022-01-27", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success"), style={"textAlign": "center"}),
                    html.Td("Kirsteen Cameron", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-catheter",  # unique ID
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),
                html.Tr([
                    html.Td("Targeted Temperature Management TTM Post Resuscitated Cardiac Arrest", style={"textAlign": "left"}),
                    html.Td(html.B("Nursing"), style={"textAlign": "center"}),
                    html.Td("2022-05-30", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success"), style={"textAlign": "center"}),
                    html.Td("Jessica Brown", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-ttm",  # unique ID
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),
                html.Tr([
                    html.Td("Fall Prevention Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Surgery"), style={"textAlign": "center"}),
                    html.Td("2022-03-15", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success"), style={"textAlign": "center"}),
                    html.Td("Jane Smith", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-fall",   # unique ID
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),
                html.Tr([
                    html.Td("Infection Control Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Infection Control"), style={"textAlign": "center"}),
                    html.Td("2021-11-22", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Inactive", color="danger"), style={"textAlign": "center"}),
                    html.Td("John Doe", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-infection",  # unique ID
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),
                html.Tr([
                    html.Td("Medication Administration Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Nursing"), style={"textAlign": "center"}),
                    html.Td("2022-06-10", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success"), style={"textAlign": "center"}),
                    html.Td("Jill Johnson", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-meds",  # unique ID
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),
                html.Tr([
                    html.Td("Wound Care Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Nursing"), style={"textAlign": "center"}),
                    html.Td("2022-01-05", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success", className="p-2", style={"fontSize": "14px"}), style={"textAlign": "center"}),
                    html.Td("Julia Black", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-wound",
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),

                html.Tr([
                    html.Td("Emergency Preparedness Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Emergency"), style={"textAlign": "center"}),
                    html.Td("2021-12-20", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success", className="p-2", style={"fontSize": "14px"}), style={"textAlign": "center"}),
                    html.Td("Justin Blue", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-emergency",
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),

                html.Tr([
                    html.Td("Pain Management Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Orthopedic"), style={"textAlign": "center"}),
                    html.Td("2022-04-18", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success", className="p-2", style={"fontSize": "14px"}), style={"textAlign": "center"}),
                    html.Td("Jeremy Green", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-pain",
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),

                html.Tr([
                    html.Td("Quality Improvement Policy and Procedure", style={"textAlign": "left"}),
                    html.Td(html.B("Quality"), style={"textAlign": "center"}),
                    html.Td("2022-02-14", style={"textAlign": "center"}),
                    html.Td(dbc.Badge("Active", color="success", className="p-2", style={"fontSize": "14px"}), style={"textAlign": "center"}),
                    html.Td("Jim Davis", style={"textAlign": "center"}),
                    html.Td(
                        dbc.Button(
                            "View",
                            id="view-pdf-quality",
                            color="link",
                            style={"padding": "0"},
                            n_clicks=0
                        ),
                        style={"textAlign": "center"}
                    ),
                ]),
            ])
        ],
        bordered=True,
        striped=True,
        hover=True,
        responsive=True,
        style={"marginTop": "20px"}
    )

def build_pdf_viewer_layout(pdf_url):
    """
    pdf_url is a path like "/data/Targeted-Temperature-Management-TTM-Post-Resusciated-Cardic-Arrest.pdf"
    """
    return html.Div(
        [
            # 'Back' button
            dbc.Button(
                "Back to Table",
                id="back-to-table",
                color="secondary",
                style={"marginBottom": "15px"}
            ),
            # PDF embed
            html.Embed(
                src=pdf_url,
                type="application/pdf",
                width="100%",
                height="100%"
            ),
        ],
        style={"height": "90vh", "overflow": "hidden", "marginTop": "20px"}
    )

results_page_layout = dbc.Container(
    [
        dcc.Store(id="selected-pdf", data=None),

        html.Div([
            dcc.Link(
                html.Img(
                    src="/assets/back.png",
                    style={
                        "width": "20px",
                        "height": "20px",
                        "position": "absolute",
                        "top": "10px",
                        "left": "20px",
                        "zIndex": "9999",
                        "cursor": "pointer"
                    }
                ),
                href='/'
            ),
            dcc.Link(
                html.Img(
                    src="/assets/home_button.png",
                    style={
                        "width": "23px",
                        "height": "21px",
                        "position": "absolute",
                        "top": "14px",
                        "right": "20px",
                        "zIndex": "9999",
                        "cursor": "pointer"
                    }
                ),
                href='/'
            )
        ]),

        # The main row => left: table or PDF viewer, right: chat
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id="left-content",
                        style={
                            "height": "100vh",  
                            "overflow": "auto",  
                        }
                    ),
                    width=6
                ),
                dbc.Col(
                    chatbox_layout(),
                    width=6,
                    style={
                        "height": "100vh",  
                        "overflow": "auto"  
                    }
                ),
            ],
            justify="start",
            style={
                "height": "100vh"  
            }
        ),
    ],
    fluid=True,
    style={
        "padding": "20px",
        "backgroundColor": "#ffffff",
        "borderRadius": "10px",
        "position": "relative",
        "height": "100vh" 
    }
)


PDF_PATH_DEFAULT = "/data/Targeted-Temperature-Management-TTM-Post-Resusciated-Cardic-Arrest.pdf"
PDF_PATH_CATHETER = "/data/urinary-catheterisation-adultsfinal.pdf"

@callback(
    Output("selected-pdf", "data", allow_duplicate=True),
    [
        Input("view-pdf-fall", "n_clicks"),
        Input("view-pdf-ttm", "n_clicks"),
        Input("view-pdf-infection", "n_clicks"),
        Input("view-pdf-catheter", "n_clicks"),
        Input("view-pdf-meds", "n_clicks"),
        Input("view-pdf-wound", "n_clicks"),
        Input("view-pdf-emergency", "n_clicks"),
        Input("view-pdf-pain", "n_clicks"),
        Input("view-pdf-quality", "n_clicks"),
    ],
    prevent_initial_call=True
)
def open_any_pdf(fall_btn, ttm_btn, infection_btn, meds_btn, catheter_btn, wound_btn, 
                 emerg_btn, pain_btn, quality_btn):
    """
    Decide which PDF to display based on which 'View' button was clicked.
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        return None
    
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # For demonstration, we’ll show:
    # - PDF_PATH_CATHETER if 'view-pdf-catheter' triggered
    # - PDF_PATH_DEFAULT for all the other rows
    if triggered_id == "view-pdf-catheter":
        return PDF_PATH_CATHETER
    else:
        return PDF_PATH_DEFAULT

# B) Clicking "Back to Table" sets selected-pdf to None
@callback(
    Output("selected-pdf", "data", allow_duplicate=True),
    Input("back-to-table", "n_clicks"),
    State("selected-pdf", "data"),
    prevent_initial_call=True
)
def back_to_table(n_clicks, current_pdf):
    if n_clicks and current_pdf is not None:
        return None
    return current_pdf


# C) Whenever selected-pdf changes, decide whether to show table or PDF
@callback(
    Output("left-content", "children"),
    Input("selected-pdf", "data")
)
def render_left_side(selected_pdf):
    """
    If selected_pdf is None => table layout
    Else => PDF viewer
    """
    if selected_pdf is None:
        return build_table_layout()
    else:
        return build_pdf_viewer_layout(selected_pdf)
