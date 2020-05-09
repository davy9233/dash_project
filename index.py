import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import article, vente, conseil, intArt

jumbotron = dbc.Jumbotron(
    [
        html.H1("Jumbotron", className="display-3"),
        html.P(
            "Use a jumbotron to call attention to "
            "featured content or information.",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "Jumbotrons use utility classes for typography and "
            "spacing to suit the larger container."
        ),
        html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ]
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    jumbotron,
    dcc.Link('aller a la page article', href='/apps/article'),
    html.Br(),
    dcc.Link('aller a la page conseil', href='/apps/conseil'),
    html.Br(),
    dcc.Link('aller a la page ventes', href='/apps/vente'),
    
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/article':
        return article.layout
    elif pathname == '/apps/vente':
        return vente.layout
    elif pathname == '/apps/conseil':
        return conseil.layout
    elif pathname == '/apps/intArt':
        return intArt.layout
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True)