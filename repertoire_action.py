import repertoire_utils_text as repertoire_utils


# Specification client:

def get_rep():
    return repertoire_utils.get_rep()


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


def lister_tous_les_contacts(repertoire):
    return repertoire_utils.lister_tous_les_contacts(repertoire)
