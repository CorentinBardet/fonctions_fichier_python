from repertoire_action import get_rep, action_recherche_du_contact, action_supression_du_contact, action_ajout_du_contact


def lister_contact(repertoire):
        print(repertoire)

def ajouter_contact_forme(repertoire):
    nom = input("Ajouter le nom du contact: ")
    numero = input("Ajouter le numero de telephone: ")
    adresse = input("Ajouter l'adresse du contact: ")
    action_ajout_du_contact(repertoire, nom, numero, adresse)

def suprimer_contact(repertoire):
    nom_supprimer = input("Quel contact souhaitez-vous supprimer: ")
    action_supression_du_contact(repertoire, nom_supprimer)

def rechercher_contact(repertoire):
    rechercher_contact = input("Quel nom à rechercher: ")
    print(action_recherche_du_contact(repertoire, rechercher_contact))


while True:
    repertoire = get_rep()
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
