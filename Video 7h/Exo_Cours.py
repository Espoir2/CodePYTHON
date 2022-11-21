
#-----*****-----*****NOUVELLES FONCTIONS*****-----*****-----#
# sourcery skip: boolean-if-exp-identity, remove-redundant-fstring, remove-unnecessary-cast, simplify-fstring-formatting, use-fstring-for-formatting
"""
issubclass(bool, int)
bool()
id(nom_de_variable)
type()
round()
sum()
sleep()
reversed()
"""

"""
#-----*****-----*****CHAINES DE CARACTERES*****-----*****-----#

#-----CARACTERES SPECIAUX-----#
print("C'est trop cool \u2764")
print("----------")

print("Je peut également aller à la \n ligne")
print("----------")


#-----CASSE DES CHAINE DE CARATERES-----#
print("Grands caracteres".upper())
print("----------")

print("PETITS CARACTERES".lower())
print("----------")

print("bonjour tout le monde".capitalize())
print("----------")

print("bonjour tout le monde".title())
print("----------")


#-----REMPLACER DES ELEMENTS-----#
print("bonjour tout le monde".replace("jour", "soir").replace(" ", "*"))
print("----------")

print(" bonjour ".strip())
print(" bonjour ".strip(" brou"))
print(" bonjour ".rstrip(" brou"))
print(" bonjour ".lstrip(" brou"))
print("----------")

#-----SEPARER ET JOINDRE-----#
print("1, 2, 3, 4, 5".split(", "))
print(", ".join("1, 2, 3, 4, 5".split(", ")))
print("----------")

#-----REMPLIR DE ZEROS-----#
print("1".zfill(3))
print("51".zfill(3))
print("178".zfill(3))
print("python".zfill(9))
print("----------")


#-----METHODES << is >>-----# Can be used with previous methods
print("Grands caracteres".isupper())
print("----------")

print("PETITS CARACTERES".islower())
print("----------")

print("1a".isdigit())
print("----------")

print("01".isdigit())
print("----------")

#-----COMPTER LES OCCURENCES-----#
print("bonjour le jour".count("jour"))
print("bonjour le jour".count(" jour"))
print("----------")


#-----TROUVER DES ELEMENTS-----#
print("bonjour le jour".find("jour"))
print("bonjour le jour".rfind("jour"))
print("bonjour le jour".index("jour"))
print("----------")

print("bonjour le jour".find("soir"))
#print("bonjour le jour".index("soir"))
print("----------")

#-----CHERCHJER AU DEBUR ET A LA FIN-----#
print("image.png".endswith("png"))
print("image.png".endswith("jpg"))
print("video".startswith("video"))
print("image".startswith("video"))
print("----------")

#-----****-----*****LES OPERATEURS****-----****-----#
# is != == 

#-----****-----*****FORMATAGE*****-----*****-----#
print("Premiere insertion {}, deuxieme insertion {} ".format(1, 2))
print("----------")

print("Premiere insertion {0}, deuxieme insertion {0} ".format("indice"))
print("----------")

print("Premiere insertion {1}, deuxieme insertion {0} ".format("indice1", "indice2"))
print("----------")

print("Premiere insertion {ins1}, deuxieme insertion {ins2} ".format(ins1 = "indice1", ins2 = "indice2"))
print("----------")

#-----****-----*****LES STRUCTURES CONDITIONNELES*****-----*****-----#
age = 20
majeur = True if age >= 18 else False  # ou majeur = age >= 18
print(majeur)
print("----------")

#-----****-----*****MODULE RANDOM*****-----*****-----#
from random import *
r = randint(0, 5)
print(r)
print("----------")

a = uniform(0, 2)
print(a)
print("----------")

b = randrange(5)
print(b)
print("----------")

c = randrange(0, 101, 10)
print(c)
print("----------")

#-----****-----*****MODULE OS*****-----*****-----#
from os import *
chemin = "D:\Mes FORMATIONS\CODING\PYTHON"
dossier_test = path.join(chemin, "dossier_test", "test")
print(dossier_test)
makedirs(dossier_test, exist_ok=True) # ou if not path.exists(dossier_test):
print("----------")

# removedirs(dossier_test) --> Pour supprimer dossier_test          !! if path.exists(dossier_test):


# [ASTUCES] --> dir() et help() ET callable()
from pprint import pprint

pprint(dir())
print("----------")

pprint(dir(randint))
print("----------")

help(random)
print("----------")

help(randint)
print("----------")
"""
#-----****-----*****LISTES*****-----*****-----#
# Methods : append(Valeur) - extend([liste]) - remove(valeur) - pop(index) - clear()
# Récupérer un élément : indices 0 1 2 ... / -1(dernier) -2(avant-dernier) ... 

from unittest import result


my_list = [False, 2, 3, 4, "cool", 6, 7, 8, 9, True]
print(my_list[:])
print("----------")

print(my_list[:3])
print("----------")

print(my_list[1:3])
print("----------")

print(my_list[:-1])
print("----------")

print(my_list[-1])
print("----------")

print(my_list[2:])
print("----------")

print(my_list[1::2]) # Afficher la liste a partir de id 1 par bon de 2
print("----------")

print(my_list[2:-1:2])
print("----------")

print(my_list[::-1]) # Afficher la liste par bon de -1 (INVERSER)
print("----------")

print(my_list.index(True))
print("----------")

print(my_list.count(True)) 
print("----------")

my_list2 = ["z", "a", "b","e",  "c"]
my_list3 = [9, 1, 4,  2, 3]

my_list2.sort()
my_list3.sort()

my_list2_trie = sorted(my_list2)
my_list3_trie = sorted(my_list3)

print(my_list2)
print(my_list3)

print("----------")

print(my_list2_trie)
print(my_list3_trie)
print("----------")

my_list.reverse()
print(my_list)

result_= "*".join(my_list2)
print(result_)

chaine = "Voila ma chaine de caractere"
chaine = chaine.split()
print(chaine)

#-----****-----*****BOUCLES*****-----*****-----#
# continue --> Passer à la prochaine ittération
# break --> Sortir dr la boucle
list_comprehension = [i for i in my_list3 if i >= 4]
print(list_comprehension)
list_comprehension2 = [i if i%2==0 else -i for i in my_list3]
print(list_comprehension2)