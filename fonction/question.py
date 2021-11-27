import random
from fonction.db import ouvrir_db

def question():
    ##conexion à la base de donnee
    db = ouvrir_db()

    ##création d'un objet curseur qu'on peut parcourir pour avoir les enregistrement de la table
    curseur = db.execute("SELECT * FROM Main_word")
    liste_des_mot = []

    ##on parcours les enregistrement de la table pour les mettre dans une liste
    for tuple in curseur:
        liste_des_mot.append(tuple)

    while len(liste_des_mot) != 0:
        couple = liste_des_mot.pop(random.randrange(len(liste_des_mot)))

        reponse = input(f"qu'elle est la traduction de {couple[0]}")
        if reponse == couple[1]:
            print("bonne reponse tu es un génie connard")
        else:
            print(f"tu est une sous merde kevin c'est bien sur {couple[1]}")





    db.close()