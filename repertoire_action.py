import repertoire_utils_dict as repertoire_utils

repertoire = []

def action_ajout_du_contact(repertoire, nom, numero, adresse):
    repertoire.append({"nom": nom, "numero": numero, "adresse": adresse})

def action_supression_du_contact(repertoire, nom_supprimer):
    for contact in repertoire:
        if contact["nom"] == nom_supprimer:
            repertoire.remove(contact)

def action_recherche_du_contact(repertoire, nom):
    results =[]
    for contact in repertoire:
        if contact["nom"] == nom:
            results.append(contact)
    return results



#Spécifications clients :

def get_rep():
    repertoire_utils.get_rep()

def ajouter_personne(repertoire, nom=None, telephone=None, adresse=None):
    personne= {"nom": nom, "telephone": telephone, "adresse": adresse}
    repertoire_utils.append_rep(repertoire, personne)
    return repertoire

def supprimer_personne(repertoire, nom):
    repertoire_utils.del_rep(repertoire, nom)
    return repertoire

def chercher_personnes(repertoire, nom=None, telephone=None, adresse=None):
    results = []
    for contact in repertoire:
        if contact["nom"] == nom:
            results.append(contact)
        if contact["telephone"] == telephone:
            results.append(contact)
        if contact["adresse"] == adresse:
            results.append(contact)
    return results

