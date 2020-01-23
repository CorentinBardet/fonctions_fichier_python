import json


def get_rep():
    data_repertoire = open("data_repertoire.txt", "r")
    repertoire = json.load(data_repertoire)
    data_repertoire.close()
    return repertoire


def append_rep(repertoire, personne):
    repertoire.append(personne)
    with open("data_repertoire.txt", "w") as data_repertoire:
        data_repertoire.write(json.dumps(repertoire))


def del_rep(repertoire, personne):
    for contact in repertoire:
        if contact["nom"] == personne:
            repertoire.remove(contact)
            with open("data_repertoire.txt", "w") as data_repertoire:
                data_repertoire.write(json.dumps(repertoire))


def lister_tous_les_contacts(repertoire):
    contacts = []
    for contact in repertoire:
        contacts.append(contact)
    return contacts
