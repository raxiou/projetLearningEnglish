import sqlite3
def ouvrir_db():
    ##conexion à la base de donnee
    db = sqlite3.connect('vocabulaire.db')
    # activation contrainte clé étranger
    db.execute("PRAGMA foreign_keys = ON")

    return db


def creation_de_la_table():
    db = ouvrir_db()
    #destruction de la table si elle existe
    db.execute("DROP TABLE IF EXISTS Main_word")

    #crée la table
    db.execute('''
    CREATE TABLE Main_word(
    translate text not null,
    french_word text not null)''')

    db.commit()
    db.close()

