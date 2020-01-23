#creer une liste

list = ["nom", "prenom", "age"]
print(list)

# ajoute relement a une liste

list.append("poids")
print(list)

# existence d'un élement d'une liste est vérifiée

element = "nom"
for element in list:
    print(element)

# suprimer un element

del list[0]
print(list)

list.remove("age")
print(list)

# inserer element

list.insert(2, "age")
print(list)

# suprimer un element d'une liste

list.pop(2)
print(list)

# fusionner 2 listes

list2 = ["24", "12", "45"]
list.extend(list2)
print(list)

# affecter un element d'une liste à une variable "n"

n = list[2]
print(n)

# liste d'entier est trié

list_nombre = [10, 50, 65, 45]
list_nombre.sort()
print(list_nombre)

# liste slice

list3 = list2[1:3]
print(list3)


myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
myList2 = myList[-5:]
print(myList)
print(myList2)

# liste crée par copie du autre liste

list_nombre_2 = list_nombre
print(list_nombre_2)

# liste modifié a travers la premiere et resultat affiché par la seconde

list_nombre.append(12)
print(list_nombre_2)