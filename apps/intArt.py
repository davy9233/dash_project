import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import mysql.connector
from app import app

form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("nom", className="mr-2"),
                dbc.Input(type="text", placeholder="Article"),
            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                dbc.Label("gencod", className="mr-2"),
                dbc.Input(type="text", placeholder="gencod(14 chiffres)"),
            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                dbc.Label("designation", className="mr-2"),
                dbc.Input(type="text", placeholder="Resume"),
            ],
            className="mr-3",
        ),
        dbc.Button("Valider", color="primary"),
    ],
    inline=True,
)


layout = html.Div([
    html.H3('integration articles'),
    form,
    html.Div(id='vente-display-value'),
    dcc.Link('aller aux articles', href='/apps/article'),
    html.Br(),
    dcc.Link('aller aux vente', href='/apps/vente'),
    html.Br(),
    dcc.Link('Retour accueil', href='/'),
    ])


