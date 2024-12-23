import dash
import dash_bootstrap_components as dbc
import flask
from dash import dcc, html, callback, no_update
from dash.dependencies import Output, Input, State

# Import layouts from other pages
from pages.search_page import search_page_layout
from pages.results_page import results_page_layout
from pages.document_page import document_page_layout  # Import the document layout

# Dash app setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
server = app.server
@server.route('/documents/<path:filename>')
def serve_document(filename):     
    return flask.send_from_directory('documents', filename)

# Main app layout with dynamic content
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Manages the URL routing
    dcc.Store(id='search-term', storage_type='session'),  # Store search term in session storage
    html.Div(id='page-content')
])

# Callback to update the page based on URL path
@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/results':
        return results_page_layout
    elif pathname.startswith('/document/'):
        # Extract the document name from the pathname
        document_name = pathname.split('/')[-1]
        return document_page_layout(document_name)  # Display the document layout with the document name
    else:
        return search_page_layout

# Callback to navigate to the results page and store the search term
@callback(
    Output('url', 'pathname'),
    Output('search-term', 'data'),
    Input('search-button', 'n_clicks'),
    State('search-input', 'value')
)
def go_to_results(n_clicks, search_term):
    if n_clicks and search_term:
        return '/results', search_term
    return no_update, no_update

# Callback to display the search term on the results page
@callback(
    Output('results-header', 'children'),
    Input('search-term', 'data')
)
def update_results_header(search_term):
    if search_term:
        return f"Search Results for '{search_term}'"
    return "Search Results"

if __name__ == "__main__":
    app.run_server(debug=True)
