 
# Exo 1
# nom = input("Quel est votre nom? ")
# age = input("Quel est votre age? ")
# print("Vous êtes " + nom + ", et vous avez " + age)

# str->int :  int()
# int->str :  str()



# Exo 2
# nom = input("Quel est votre nom? ")
# age = input("Quel est votre age? ")
# try:
#     age_prochain = int(age) + 1
# except:
#     print ("Veuillez entrer un nombre pour votre âge")
# else:
#     print("Vous êtes " + nom + ", et vous avez " + age + " ans")
#     print("L'an prochain vous aurrez "  + str(age_prochain) + " ans")


# Exo 3
"""nom = ""
while nom == "":
    nom = input("Quel est votre nom? ")
    print("Veuillez bien entrer votre nom")

age = 0
while age == 0:
    age_str = input("Quel est votre age? ")
    try:
        age = int(age_str)
    except:
        print ("Veuillez entrer un nombre pour votre âge")
    

print("Vous êtes " + nom + ", et vous avez " + str(age) + " ans")
print("L'an prochain vous aurrez "  + str(age + 1) + " ans")
"""

# Exo 4 : Function


"""
def demander_nom():
    nom_local = ""
    while nom_local == "":
        nom_local = input("Quel est votre nom? ")
        print("Veuillez bien entrer votre nom")
    return nom_local

def demander_age():
    age_local = 0
    while age_local == 0:
        age_str = input("Quel est votre age? ")
        try:
            age_local = int(age_str)
        except:
            print ("Veuillez entrer un nombre pour votre âge")
    return age_local


def afficher_resultats():
    print("Vous êtes " + nom + ", et vous avez " + str(age) + " ans")
    print("L'an prochain vous aurrez "  + str(age + 1) + " ans")


nom = demander_nom()
age = demander_age()
afficher_resultats()
"""

# Utiliser global variable pour utiliser une variable globale à l'intérieur d'une fonction




#  Exo 5

"""

def demander_nom():
    nom_local = ""
    while nom_local == "":
        nom_local = input("Quel est votre nom? ")
        print("Veuillez bien entrer votre nom")
    return nom_local

def demander_age(nom_personne):
    age_local = 0
    while age_local == 0:
        age_str = input(nom_personne + " Quel est votre age? ")
        try:
            age_local = int(age_str)
        except:
            print (nom_personne + " Veuillez entrer un nombre pour votre âge")
    return age_local


def afficher_resultats(nom , age):
    print("Vous êtes " + nom + ", et vous avez " + str(age) + " ans")
    print("L'an prochain vous aurrez "  + str(age + 1) + " ans")


nom1 = demander_nom()
nom2 = demander_nom()
age1 = demander_age(nom1)
age2 = demander_age(nom2)
afficher_resultats(nom1, age1)
afficher_resultats(nom2, age2)


"""




# Exo 6 : MAIN

def demander_nom():
    nom_local = ""
    while nom_local == "":
        nom_local = input("Quel est votre nom? ")
        print("Veuillez bien entrer votre nom")
    return nom_local

def demander_age(nom_personne):
    age_local = 0
    while age_local == 0:
        age_str = input(nom_personne + " Quel est votre age? ")
        try:
            age_local = int(age_str)
        except:
            print (nom_personne + " Veuillez entrer un nombre pour votre âge")
    return age_local


def afficher_resultats(nom , age):
    print()
    print("Vous êtes " + nom + ", et vous avez " + str(age) + " ans")
    print("L'an prochain vous aurrez "  + str(age + 1) + " ans")

    if age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Vous êtes juste majeur:Félicitation")
    elif age <= 10:
        print("Vous êtes junior")
    elif age >= 60:
        print("Vous êtes senior")
    elif age < 18:
        print("Vous êtes mineur")
    else:
        print("Vous êtes majeur")

        


nom1 = demander_nom()
nom2 = demander_nom()
nom3 = demander_nom()
nom4 = demander_nom()
nom5 = demander_nom()
nom6 = demander_nom()
age1 = demander_age(nom1)
age2 = demander_age(nom2)
age3 = demander_age(nom3)
age4 = demander_age(nom4)
age5 = demander_age(nom5)
age6 = demander_age(nom6)
afficher_resultats(nom1, age1)
afficher_resultats(nom2, age2)
afficher_resultats(nom3, age3)
afficher_resultats(nom4, age4)
afficher_resultats(nom5, age5)
afficher_resultats(nom6, age6)     
# Exo_cours

for i in range(0, 5):
    print(i)

# Syntaxe pour indroduire des variables dans des chaines de caractères
""" print(f"chaine de caractères {variable1} chaine de caractères {variable2} chaine de caractères ")
    print("chaine de caractères %s chaine de caractères %s chaine de caractères" % (variable1, variable2) )
"""

# Print sur plusieurs ligne

#print(""" 
#Là c'est vraiment cool
#J'arrive à mettre mes print sur plusieurs lignes

#Je pourrai facilement copier et coller du texte
#""")     

# pour donner des paramètres àla fonction print: print(paramètre1, paramètre2, paramètre3)