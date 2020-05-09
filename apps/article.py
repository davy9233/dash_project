import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import mysql.connector

from app import app

conn = mysql.connector.connect(host="localhost", user="davy", passwd="davy", db="magasin")
cursor = conn.cursor()
cursor.execute('select * from articles');
total = cursor.fetchall()
liste_art=[]
for row in total :
    liste_art.append({'label':row[1],'value': row[0]})

import dash_bootstrap_components as dbc
import dash_html_components as html

card = dbc.Card(
    [
        dbc.CardImg(src="", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

layout = html.Div([
    html.H3('Articles'),
    dcc.Dropdown(
        id='article-dropdown',
        options=liste_art
    ),
    html.Div(
        [
        dbc.Row(
            [
            dbc.Col(card),
            dbc.Col(dcc.Graph())
            ]),
        ]), 
    html.Div(id='article-display-value'),
    dcc.Link('Go to App 2', href='/apps/vente'),
    html.Br(),
    dcc.Link("creation d'articles", href='/apps/intArt'),
    html.Br(),
    dcc.Link('aller aux conseil', href='/apps/conseil'),
    html.Br(),
    dcc.Link('Retour accueil', href='/'),
])



@app.callback(
    Output('article-display-value', 'children'),
    [Input('article-dropdown', 'value')])
def display_value(value):
    if value == None :
        message = "Vous n'avez rien selectionne"
    else :
        message=""
    return message