repertoire = {}

while True:
    option = input("Choisir une option (- taper L pour lister - taper A pour ajouter - taper S pour supprimer - taper R pour rechercher un contact): ")
    if option == "L":
        for nom_contact, numero_contact in repertoire.items():
            print("Contact: {} / Numero: {}.".format(nom_contact, numero_contact))
    elif option == "A":
        ajouter_nom = input("Ajouter le nom du contact: ")
        ajouter_numero = input("Ajouter le numero de telephone: ")
        repertoire[ajouter_nom] = ajouter_numero
    elif option == "S":
        supprimer = input("Quel contact souhaitez-vous supprimer: ")
        del repertoire[supprimer]
    elif option == "R":
        rechercher_contact = input("Quel nom à rechercher: ")
        for nom_contact, numero_contact in repertoire.items():
            if rechercher_contact in nom_contact:
                print("Contact: {} / Numero: {}.".format(nom_contact, numero_contact))
