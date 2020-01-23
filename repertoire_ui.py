import repertoire_action as action
from terminaltables import AsciiTable

def lister_tous_les_contact(repertoire):
    afficher_contacts(action.lister_tous_les_contacts(repertoire))


def afficher_contacts(contacts):
    table_content = [["nom", "telephone", "adresse"]]
    for contact in contacts:
        table_content.append([contact["nom"], contact["telephone"], contact["adresse"]])
    print(AsciiTable(table_content).table)


def ajouter_contact_forme(repertoire):
    nom = input("Ajouter le nom du contact: ")
    numero = input("Ajouter le numero de telephone: ")
    adresse = input("Ajouter l'adresse du contact: ")
    action.ajouter_personne(repertoire, nom, numero, adresse)


def suprimer_contact(repertoire):
    nom_supprimer = input("Quel contact souhaitez-vous supprimer: ")
    action.supprimer_personne(repertoire, nom_supprimer)


def rechercher_contact(repertoire):
    rechercher_contact = input("Quel nom à rechercher: ")
    rechercher_telephone = input("Quel numero a rechercher: ")
    rechercher_adresse = input("Quelle adresse a rechercher: ")
    contacts = action.chercher_personnes(repertoire, rechercher_contact, rechercher_telephone, rechercher_adresse)
    afficher_contacts(contacts)

while True:
    repertoire = action.get_rep()
    option = input(
        "Choisir une option (taper -(L)ister -(A)jouter -(S)upprimer -(R)echercher un contact -(Q)uitter: ").upper()
    if option == "L":
        lister_tous_les_contact(repertoire)
    elif option == "A":
        ajouter_contact_forme(repertoire)
    elif option == "S":
        suprimer_contact(repertoire)
    elif option == "R":
        rechercher_contact(repertoire)
    elif option == "Q":
        break
