import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('conseil'),
    html.Div(id='vente-display-value'),
    dcc.Link('aller aux articles', href='/apps/article'),
    html.Br(),
    dcc.Link('aller aux vente', href='/apps/vente'),
    html.Br(),
    dcc.Link('Retour accueil', href='/'),
    ])