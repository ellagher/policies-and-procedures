# import dash_bootstrap_components as dbc
# from dash import html, dcc
# import flask

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
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Infection Control Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Infection Control"), style={"textAlign": "center"}),
#                             html.Td("2021-11-22", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Inactive", color="danger", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("John Doe", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Medication Administration Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Nursing"), style={"textAlign": "center"}),
#                             html.Td("2022-06-10", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jill Johnson", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Wound Care Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Nursing"), style={"textAlign": "center"}),
#                             html.Td("2022-01-05", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Julia Black", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Emergency Preparedness Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Emergency"), style={"textAlign": "center"}),
#                             html.Td("2021-12-20", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Justin Blue", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Pain Management Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Orthopedic"), style={"textAlign": "center"}),
#                             html.Td("2022-04-18", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jeremy Green", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Targeted Temperature Management TTM Post Resuscitated Cardiac Arrest",
#                                     style={"textAlign": "left"}),
#                             html.Td(html.B("Nursing"), style={"textAlign": "center"}),
#                             html.Td("2022-05-30", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jessica Brown", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                         html.Tr([
#                             html.Td("Quality Improvement Policy and Procedure", style={"textAlign": "left"}),
#                             html.Td(html.B("Quality"), style={"textAlign": "center"}),
#                             html.Td("2022-02-14", style={"textAlign": "center"}),
#                             html.Td(dbc.Badge("Active", color="success", className="p-2",
#                                                style={"fontSize": "14px"}), style={"textAlign": "center"}),
#                             html.Td("Jim Davis", style={"textAlign": "center"}),
#                             html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
#                         ]),
#                     ])
#                 ], bordered=True, striped=True, hover=True, responsive=True, style={"marginTop": "20px"})
#             ],
#             width=6  # Occupies half of the page width
#         ),
#         dbc.Col([], width=6)  # Empty column to fill the right half
#     ], justify="start"),
# ], fluid=True, style={
#     "padding": "20px",
#     "backgroundColor": "#ffffff",
#     "borderRadius": "10px",
#     "position": "relative"  # Necessary for absolute positioning of buttons
# })

import dash_bootstrap_components as dbc
from dash import html, dcc
import flask
from pages.chatbox import chatbox_layout


# Table layout for displaying search results
results_page_layout = dbc.Container([
    # Back and Home Buttons using dcc.Link
    html.Div([
        dcc.Link(
            html.Img(
                src="/assets/back.png",
                style={
                    "width": "30px",
                    "height": "30px",
                    "position": "absolute",
                    "top": "20px",
                    "left": "20px",
                    "zIndex": "9999",
                    "cursor": "pointer"
                }
            ),
            href='/'  # Navigates to the search page
        ),
        dcc.Link(
            html.Img(
                src="/assets/home_button.png",
                style={
                    "width": "33px",
                    "height": "31px",
                    "position": "absolute",
                    "top": "20px",
                    "right": "20px",
                    "zIndex": "9999",
                    "cursor": "pointer"
                }
            ),
            href='/'  # Navigates to the home page (search page)
        )
    ]),
    dbc.Row([
        dbc.Col(
            [
                # Table with headers and rows for each document
                dbc.Table([
                    html.Thead(html.Tr([
                        html.Th("Title", style={"textAlign": "left", "width": "30%"}),
                        html.Th("Department", style={"textAlign": "center", "width": "15%"}),
                        html.Th("Revision Date", style={"textAlign": "center", "width": "15%"}),
                        html.Th("Status", style={"textAlign": "center", "width": "10%"}),
                        html.Th("Last Modified By", style={"textAlign": "center", "width": "15%"}),
                        html.Th("Action", style={"textAlign": "center", "width": "15%"})
                    ])),
                    html.Tbody([
                        html.Tr([
                            html.Td("Fall Prevention Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Surgery"), style={"textAlign": "center"}),
                            html.Td("2022-03-15", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Jane Smith", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Infection Control Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Infection Control"), style={"textAlign": "center"}),
                            html.Td("2021-11-22", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Inactive", color="danger", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("John Doe", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Medication Administration Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Nursing"), style={"textAlign": "center"}),
                            html.Td("2022-06-10", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Jill Johnson", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Wound Care Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Nursing"), style={"textAlign": "center"}),
                            html.Td("2022-01-05", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Julia Black", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Emergency Preparedness Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Emergency"), style={"textAlign": "center"}),
                            html.Td("2021-12-20", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Justin Blue", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Pain Management Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Orthopedic"), style={"textAlign": "center"}),
                            html.Td("2022-04-18", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Jeremy Green", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Targeted Temperature Management TTM Post Resuscitated Cardiac Arrest",
                                    style={"textAlign": "left"}),
                            html.Td(html.B("Nursing"), style={"textAlign": "center"}),
                            html.Td("2022-05-30", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Jessica Brown", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                        html.Tr([
                            html.Td("Quality Improvement Policy and Procedure", style={"textAlign": "left"}),
                            html.Td(html.B("Quality"), style={"textAlign": "center"}),
                            html.Td("2022-02-14", style={"textAlign": "center"}),
                            html.Td(dbc.Badge("Active", color="success", className="p-2",
                                               style={"fontSize": "14px"}), style={"textAlign": "center"}),
                            html.Td("Jim Davis", style={"textAlign": "center"}),
                            html.Td(html.A("View", href="/documents/document.txt", style={"color": "blue"}))
                        ]),
                    ])
                ], bordered=True, striped=True, hover=True, responsive=True, style={"marginTop": "20px"})
            ],
            width=6  # Occupies half of the page width
        ),
        dbc.Col(chatbox_layout(), width=6)  # Empty column to fill the right half
    ], justify="start"),
], fluid=True, style={
    "padding": "20px",
    "backgroundColor": "#ffffff",
    "borderRadius": "10px",
    "position": "relative"  # Necessary for absolute positioning of buttons
})
