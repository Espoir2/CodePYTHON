# Exo 1 : Codez un blablateur! (Utiliser la notion de LISTE)
# LISTE IMBRIQUEE : nom_de_la_liste[index][index]
# AJOUTER : nom_de_la_liste.append ("élément")
# SUPPRIMER : del nom_de_la_liste

"""
from random import*
nom = ['Espoir', 'Nahim','Amael','Faust','Emmanuel','Timothée', 'Bernadin' ]
activites = ['travaille', 'dort','mange','chante','cuisine','code', 'joue' ]
lieu = ['à la maison', 'sous la douche','à la cuisine',"à l'aéroport",'au marché','dans la voiture', 'sur le terrain' ]

def blablateur():
    while True:
        print(choice(nom), choice(activites), choice(lieu))
        input("Appuyez sur entrée pour continuer!")
blablateur()
"""



# Cours : DICTIONNAIRES

# RECUPERER UNE VALEUR: nom_du_dictionnaire.get("clé", "message en cas d'ereur")
# RECUPERER UNE VALEUR DANS UN DICTIONNAIRE IMBRIQUE: nom_du_dictionnaire["clé"]["clé"]
# SUPPRIMER : del nom_du_dictionnaire[clé]
# nom_du_dictionnaire.keys()
# nom_du_dictionnaire.values()
# nom_du_dictionnaire.items()


# Exo 2 : Créez un dictionnaire puis afficher les différentes cle:valeur
"""
d = {'Bonjour':'Hello',
     'Jouer' : 'To play',
     'Travailler' : 'To work',
     'Livre' : 'Book',
     'Stylo' : 'Pen',
    }
for cle, valeur in d.items() : 
    print(f"{cle} : {valeur}")
"""

# Exo 3 : Créez un traducteur français -> anglais
"""
anglais = {'bonjour':'Hello',
     'jouer' : 'To play',
     'travailler' : 'To work',
     'livre' : 'Book',
     'stylo' : 'Pen',
    }

while True:
    mot = input("Entrez un mot : ")
    if mot in anglais:
        print (f"{mot} se dit {anglais[mot]} en anglais.")
    else : 
        print("Désolé, je ne comprends pas ce mot!")
"""