# repertoire_ui :

from repertoire_action import get_rep, chercher_personnes, supprimer_personne, ajouter_personne


def lister_tous_les_contacts(repertoire):
    for contact in repertoire_action.lister_tous_les_contacts(repertoire):
    print(contact)

def ajouter_contact_forme(repertoire):
    nom = input("Ajouter le nom du contact: ")
    numero = input("Ajouter le numero de telephone: ")
    adresse = input("Ajouter l'adresse du contact: ")
    ajouter_personne(repertoire, nom, numero, adresse)


def suprimer_contact(repertoire):
    nom_supprimer = input("Quel contact souhaitez-vous supprimer: ")
    supprimer_personne(repertoire, nom_supprimer)


def rechercher_contact(repertoire):
    rechercher_contact = input("Quel nom à rechercher: ")
    rechercher_telephone = input("Quel numero a rechercher: ")
    rechercher_adresse = input("Quelle adresse a rechercher: ")
    chercher_personnes(repertoire, rechercher_contact, rechercher_telephone, rechercher_adresse)

while True:
    repertoire = get_rep()
    option = input(
        "Choisir une option (- taper L pour lister - taper A pour ajouter - taper S pour supprimer - taper R pour rechercher un contact): ")
    if option == "L":
        get_rep()
    elif option == "A":
        ajouter_contact_forme(repertoire)
    elif option == "S":
        suprimer_contact(repertoire)
    elif option == "R":
        rechercher_contact(repertoire)


# repertoire_action :

import repertoire_utils_dict as repertoire_utils


# Specification client:

def get_rep():
    repertoire_utils.get_rep()


def ajouter_personne(repertoire, nom=None, telephone=None, adresse=None):
    personne = {"nom": nom, "telephone": telephone, "adresse": adresse}
    repertoire_utils.append_rep(repertoire, personne)
    return repertoire


def supprimer_personne(repertoire, nom):
    repertoire_utils.del_rep(repertoire, nom)
    return repertoire


def chercher_personnes(repertoire, nom=None, telephone=None, adresse=None):
    results = []
    for contact in repertoire:
        if contact["nom"] == nom or contact["telephone"] == telephone or contact["adresse"] == adresse:
            results.append(contact)
    return results


# repertoire_utils_dict :

repertoire = []


def get_rep():
    return repertoire


def append_rep(repertoire, personne):
    repertoire.append(personne)


def del_rep(repertoire, personne):
    for contact in repertoire:
        if contact["nom"] == personne:
            repertoire.remove(contact)


# repertoire_utils_text :

fichier = open("data_repertoire.txt", "a")
    fichier.write(repertoire.append(personne))
    fichier.close()

# tableau ascii

contact-list.append([contact["nom"], contact["tel"], contact["adresse"]])
contact_list.table = asciiTable(contact.list)

# option modifier contact

while True:
    repertoire

option_modifier = input("Souhaitez-vous modifier ce contact ? (O/N)").upper()
    if option_modifier == "O":
        demande_modif = input("Que voulez-vous supprimer ? taper -(N)om -(T)elephone -(A)dresse: ").upper()
        if demande_modif == "N":
            modifier_nom = input("Nouveau nom: ")
        elif demande_modif == "T":
            modifier_tel = input("Nouveau telephone: ")
        elif demande_modif == "A":
            mofifier_adresse = input("Nouvelle adresse: ")
