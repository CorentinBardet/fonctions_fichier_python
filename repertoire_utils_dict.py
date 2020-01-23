repertoire = []

def get_rep():
    return repertoire

def append_rep(repertoire, personne):
    repertoire.append(personne)

def del_rep(repertoire, personne):
    for contact in repertoire:
        if contact["nom"] == personne:
            repertoire.remove(contact)
