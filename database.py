import mysql.connector
import re

class Basesql:
## creation de la base de données

    def __init__(self,host,database,user,password):
        self.database=database
        self.host=host
        self.user=user
        self.password=password

#test la presence de la base et la cree si besoin
    def connect_base(self):
        try:
            conn = mysql.connector.connect(database=self.database,user=self.user)
            if conn.is_connected():
                message=f"vous etes connecté sur la base {self.database}"
            
        except mysql.connector.Error as e:
            print(e)
            if re.search('Unknown database',str(e)) != None :
                conn2 = mysql.connector.connect(host=self.host,user=self.user,password=self.password)
                mycursor = conn2.cursor()
                mycursor.execute("CREATE DATABASE MAGASIN")
                message= "la base vient d'etre créée"
            else :
                print('contacter le dev')
        return message

    def create_tables(self):
        #creation des tables
        conn = mysql.connector.connect(host=
        self.host,database=self.database,user=
        self.user,password=
        self.password)
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Articles(Id INT AUTO_INCREMENT  PRIMARY KEY, Nom VARCHAR(255), Gencod VARCHAR(255), Designation VARCHAR(255))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Clients(Id INT AUTO_INCREMENT  PRIMARY KEY, Nom VARCHAR(255), Societe VARCHAR(255), Telephone VARCHAR(255))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Commandes(Id INT AUTO_INCREMENT  PRIMARY KEY, numero INT, Article VARCHAR(255), Quantite INT, Date VARCHAR(255),FOREIGN KEY(ArticleId) REFERENCES Articles(Id))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Stock(ArticleId INT, Quantite real, Date VARCHAR(255))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Ventes(id_ventes INT AUTO_INCREMENT  PRIMARY KEY, ArticleId INT, Quantite INT, Date VARCHAR(255),FOREIGN KEY(ArticleId) REFERENCES Articles(Id))")        

