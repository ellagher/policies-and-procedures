from dash import html, dcc

def document_page_layout(document_name):
    document_links = {
        "TTM_Post_Resuscitated_Cardiac_Arrest": "data/Targeted-Temperature-Management-TTM-Post-Resusciated-Cardic-Arrest.pdf"
        # Add other documents as needed with corresponding paths
    }
    
    document_path = document_links.get(document_name, "#")
    
    return html.Div([
        html.H2("Document Viewer", style={"textAlign": "center"}),
        dcc.Link("View", href= "document.txt", target = '_blank'),
        


        html.H4(document_name.replace('_', ' '), style={"textAlign": "center"}),
        html.Embed(src=document_path, type="application/pdf", width="100%", height="800px"),
        html.Br(),
        html.A("Back to Results", href="/results", style={"display": "block", "textAlign": "center", "marginTop": "20px"})
    ])
