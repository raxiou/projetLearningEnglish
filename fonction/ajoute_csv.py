import sqlite3
import csv
from fonction.db import ouvrir_db

def ajoute_csv():

    ##importation du fichier csv(a crée avec un tableur)
    # fiche_voc = input("votre fichier de vocabulaire(en csv avec l'extension)(exemple : fiche voc.csv")

    f = open('fiche_voc.csv')
    fichierCSV = csv.reader(f)

    liste_csv = list(fichierCSV)



    ##conexion à la base de donnee
    db = ouvrir_db()



    liste_de_tuple = []
    for couple in liste_csv:
        tuple = (couple[0],couple[2])
        liste_de_tuple.append(tuple)


    db.executemany("INSERT INTO Main_word VALUES(?,?)",liste_de_tuple)
    db.commit()
    db.close()

