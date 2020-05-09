import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('articles'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='articles-display-value'),
    dcc.Link('Go to App 2', href='/apps/ventes'),
    html.Br(),
    dcc.Link('Retour accueil', href='/'),
])



@app.callback(
    Output('articles-display-value', 'children'),
    [Input('articles-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)