from repertoire_action import *

repertoire = [{"Jean","0645657895","15,rue"}]



def lister_contact(repertoire):
    for nom_contact, numero_contact in repertoire.items():
        print("Contact: {} / Numero: {}.".format(nom_contact, numero_contact))


def ajouter_contact_forme(repertoire):
    nom = input("Ajouter le nom du contact: ")
    numero = input("Ajouter le numero de telephone: ")
    adresse = input("Ajouter l'adresse du contact")
    action_ajout_du_contact(repertoire, nom, numero)

def suprimer_contact(repertoire):
    supprimer = input("Quel contact souhaitez-vous supprimer: ")
    action_supression_du_contact(repertoire, supprimer)

def rechercher_contact(repertoire):
    rechercher_contact = input("Quel nom à rechercher: ")
    action_recherche_du_contact(repertoire)

while True:

    option = input(
        "Choisir une option (- taper L pour lister - taper A pour ajouter - taper S pour supprimer - taper R pour rechercher un contact): ")
    if option == "L":
        lister_contact(repertoire)
    elif option == "A":
        ajouter_contact_forme(repertoire)
    elif option == "S":
        suprimer_contact(repertoire)
    elif option == "R":
        rechercher_contact(repertoire)
