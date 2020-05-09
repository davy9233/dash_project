import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import mysql.connector

#from app import app

conn = mysql.connector.connect(host="localhost", user="davy", passwd="davy", db="magasin")
cursor = conn.cursor()
cursor.execute('select id,nom from articles');
total = cursor.fetchall()
liste_art=[]
for row in total :
    liste_art.append({'label':row[1],'value': row[0]})
print(liste_art)
liste_art=str(liste_art)
print(type(liste_art))
print(liste_art)