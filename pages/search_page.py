import dash_bootstrap_components as dbc
from dash import dcc, html

# Header style
header_style = {
    "backgroundColor": "#1C2337",
    "padding": "10px",
    "color": "white",
    "fontSize": "24px",
    "fontWeight": "bold",
    "fontFamily": "sans-serif",
    "display": "flex",
    "alignItems": "center",
    "justifyContent": "space-between",
    "position": "relative"
}

# Title, search bar, and filter options container with background image styling
title_container_style = {
    "backgroundImage": "url('/assets/title_background.jpg')",
    "backgroundSize": "cover",
    "backgroundRepeat": "no-repeat",
    "backgroundPosition": "center top",
    "width": "70%",
    "margin": "0 auto",
    "padding": "40px 20px",
    "borderRadius": "10px",
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",
    "justifyContent": "center",
    "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
    "height": "450px",
    "object-position": "0 -100px",
}

# Image container style
image_container_style = {
    "textAlign": "center",
    "marginBottom": "20px"
}

image_style = {
    "width": "100%",
    "height": "auto",
    "display": "block"
}

text_style = {
    "marginTop": "10px",
    "fontWeight": "bold",
    "textAlign": "center"
}

# First Page Layout (Search Page with Featured Documents)
search_page_layout = html.Div([
    # Header with logo and title
    html.Div(
        [
            html.Img(src="/assets/logo.png", height="50px", style={"marginRight": "10px", "width": "150px", "height": "40px"}),
        ],
        style=header_style
    ),

    # Main content title, search bar, and filter options with background image
    html.Div(
        [
            html.H1(
            [
            "CARE C", 
            html.Img(
                src="/assets/the_o.png", 
                height="40px", 
                style={
                    "verticalAlign": "middle",
                    "position": "relative",
                    "top": "-5px"  # Adjusted value to move the image slightly lower
                }
            ), 
            "MPASS"
            ], 
            style={"fontSize": "60px", "fontWeight": "bold", "color": "black", "marginBottom": "20px", "marginTop": "150px"}
            ),
            # Search Bar
            dbc.InputGroup(
                [
                    dbc.Input(id="search-input", placeholder="Enter keywords (e.g., TTM)", type="text"),
                    dbc.Button("Search", id="search-button", color="warning"),
                ],
                style={"width": "100%", "marginTop": "20px"}
            ),
            
            # Filter Options
            html.Div(
                dbc.RadioItems(
                    options=[
                        {"label": "Keywords", "value": "keywords"},
                        {"label": "Document", "value": "document"},
                        {"label": "Department", "value": "department"},
                    ],
                    value="keywords",
                    inline=True,
                    id="filter-options",
                ),
                style={"textAlign": "center", "marginTop": "20px"}  # Added margin to separate from search bar
            ),
        ],
        style=title_container_style
    ),

    # Featured Documents Section
    html.Div([
        html.H5(
            "Featured Documents", 
            style={
                "textAlign": "left",
                "marginLeft": "16%",  # Shifted further to the right
                "marginBottom": "15px",
                "fontWeight": "bold"
            }
        ),
        dbc.Row([
            dbc.Col(html.Div([
                html.Img(src="assets/image_one.jpg", style=image_style),
                html.Div("Code Blue", style=text_style)
            ], style=image_container_style), width=2),
            dbc.Col(html.Div([
                html.Img(src="assets/image_two.jpg", style=image_style),
                html.Div("Fall Precaution", style=text_style)
            ], style=image_container_style), width=2),
            dbc.Col(html.Div([
                html.Img(src="assets/image_three.jpg", style=image_style),
                html.Div("Wound Care", style=text_style)
            ], style=image_container_style), width=2),
            dbc.Col(html.Div([
                html.Img(src="assets/image_four.jpg", style=image_style),
                html.Div("Infection Control", style=text_style)
            ], style=image_container_style), width=2),
        ], justify="center"),
        dbc.Row([
            dbc.Col(html.Div([
                html.Img(src="assets/image_five.jpg", style=image_style),
                html.Div("Code Blue", style=text_style)
            ], style=image_container_style), width=2),
            dbc.Col(html.Div([
                html.Img(src="assets/image_six.jpg", style=image_style),
                html.Div("Fall Precaution", style=text_style)
            ], style=image_container_style), width=2),
            dbc.Col(html.Div([
                html.Img(src="assets/image_seven.jpg", style=image_style),
                html.Div("Wound Care", style=text_style)
            ], style=image_container_style), width=2),
            dbc.Col(html.Div([
                html.Img(src="assets/image_eight.jpg", style=image_style),
                html.Div("Infection Control", style=text_style)
            ], style=image_container_style), width=2),
        ], justify="center"),
    ], style={"marginBottom": "40px"})
])
