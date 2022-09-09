#-*- coding:Latin-1 -*-
from audioop import reverse
from ntpath import join
from operator import indexOf, invert
from random import *
from math import *
from tkinter import *
from unittest import result
from turtle import *
from time import *
# setup(800, 600, -500, -500)
#setup(startx=0, starty=0)


#---------------------------------------- ASTUCES ----------------------------------------#
# Pour transformer une suite d'Ã©lÃ©ment sÃ©parÃ©s par des virgules en liste --> liste = list(eval(Ã©lÃ©ment1, Ã©lÃ©ment2, Ã©lÃ©ment3,))
# Pour importer des bibliothÃ¨ques de fonction --> from 'fonction' import*



#---------------------------------------- EXO PERSO ----------------------------------------#

#EXO PERSO 1 :  JEUX DE DEVINETTE DE NOMBRE
"""
print("Bienvenue dans mon jeu. Essayer de deviner le nombre que le jeu vous cache !")
liste = list(range(100))
nombre = choice(liste)
choix = 0
while choix != nombre:
    def demander_nbr():
        nbr = 0
        while nbr == 0:
            try:
                nbr_str = input("Veuillez saisir un nombre different de 0 : ")
                nbr = int(nbr_str)
            except Exception:
                print("Veuiller bien entrer un nombre svp")
        return nbr


    choix = demander_nbr()

    if choix < nombre:
        print("Essayez plus grand")
    elif choix > nombre :
        print("Essayez plus petit")
    else:
        print("Félicitations vous avez devinez le nombre!")
"""
#EXO PERSO 2 :  SOMME DE NOMBRES
"""
total = 0
for i in range(1, 1001):
    total = total + i 
print(total)
"""


#---------------------------------------- EXO DOCUMENTS ----------------------------------------#

# Exo 1 : Afficher à l'écran les 1000 premiers termes de la suite de Fibonacci
"""
a,b,c=1,1,1
while c < 1000:
    print(b, end=" ")
    a, b, c = b, a+b, c+1

"""


# Exo 2 : Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.
"""
i = 0
while i < 20 :
    result = 7 * i
    print(f"7 x {i} = {result}")
    i = i+1

"""


# Exo 3 : Écrivez un programme qui affiche une table de conversion de sommes d'argent exprimées en euros, en Franc CFA
"""

i = 1
while i < 21 :
    result = 656 * i
    print(f"{i} Euros = {result} FCFA")
    i = i+1

"""


# Exo 3 : Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au triple du terme précédent
"""
i = 0
b = 1
while i < 12:
    print(b, end=" ")
    b = b * 3
    i = i+1

"""

# Exo 4 : Écrivez un programme qui calcule le volume d'un parallélépipède rectangle dont sont fournis 
# au départ la largeur, la hauteur et la profondeur.
"""

print("Calculons ensemble le volume de votre pavé droit")
print()

longueur = 0
while longueur == 0:
    try:
        longueur_str = input("Entrer la longueur du solide en mètre, (Un nombre svp)")
        longueur = int(longueur_str)
    except:
        print("Veuiller entrer un nombre pour la longueur")
print(f"Génial, Votre solide à une longueur de {longueur} mètres. Passons à la prochaine étape!")
print()


largeur = 0
while largeur == 0:
    try:
        largeur_str = input("Entrer la largeur du solide en mètre, (Un nombre svp)")
        largeur = int(largeur_str)
    except:
        print("Veuiller entrer un nombre pour la largeur")
print(f"Génial, Votre solide à une largeur de {largeur} mètres. Passons à la prochaine étape!")
print()


hauteur = 0
while hauteur == 0:
    try:
        hauteur_str = input("Entrer la hauteur du solide en mètre, (Un nombre svp)")
        hauteur = int(hauteur_str)
    except:
        print("Veuiller entrer un nombre pour la hauteur")
print(f"Génial, Votre solide à une hauteur de {hauteur} mètres.")
print()

result = longueur * largeur * hauteur
"""
#print(f"""Le volume de votre pavé - droit est {result} mètre cube

 #                  FIN DU PROGRAMME!
#""")




# Exo 5 : Écrivez un programme qui convertit un nombre entier de secondes fourni au départ en un nombre 
# d'années, de mois, de jours, de minutes et de secondes (utilisez l'opérateur modulo : %).
"""
print("Ce programme vous aide à décomposer totalement le nombre de secondes que vous voulez")
print()
def demander_seconde():
    seconde = 0
    while seconde == 0:
        try:
            seconde_str = input("Veuillez entrer le nombre de seconde que vous voulez convertir : ")
            seconde = int(seconde_str)
        except:
            print("Veuiller entrer un nombre pour les secondes")
    return seconde

print()
seconde = demander_seconde()
année = seconde // 31536000
reste_année = seconde % 31536000
mois = reste_année // 2592000
reste_mois = reste_année % 2592000
jours = reste_mois // 86400
reste_jours = reste_mois % 86400
heures = reste_jours // 3600
reste_heure = reste_jours % 3600
minutes = reste_heure // 60
reste_minute = reste_heure % 60
print(f"{seconde} secondes fait {année} années {mois} mois {jours} jours {heures} heures {minutes} minutes {reste_minute} secondes")

"""

# Exo 6 : Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, 
# en signalant au passage (à l'aide d'une astérisque) ceux qui sont des multiples de 3. 
# Exemple : 7 14 21 * 28 35 42 * 49 ...
"""
i = 0
while i < 20 :
    result = 7 * i
    if result % 3 == 0:
        print(f"{result}*", end=" ")
    else:
        print(result, end=" ")
    i = i+1
"""




# Exo 7 : Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13, 
# mais n'affiche que ceux qui sont des multiples de 7.
"""
i = 0
while i < 50 :
    result = 13 * i
    if result % 7 == 0:
        print(f"{result}", end=" ")
    
    i = i+1

"""


# Exo 8 : Écrivez un programme qui affiche la suite de symboles suivante :
# *
# **
# ***
# ****
# *****
# ******
# *******
"""
print("Affichons quelque chose d'interressant!")
print()
print("*\n**\n***\n****\n*****\n******\n*******\n")
"""



# Exo 9 : Ecrivez un programme qui convertit un angle entré par l'utilisateur en degrés 
# en radians, minutes, secondes
"""
print("Grâce à ce programme vous allez pouvoir convertir n'importe quel angle exprimé en degrés, en radians, minutes, seconde ")
print()
def demander_angle():
    angle = 0
    while angle == 0:
        try:
            angle_str = input("Veuillez saisir l'angle que vous voulez convertir : ")
            angle = int(angle_str)
        except:
            print("Veuiller entrer un nombre pour l'angle : ")
    return angle
angle_saisi = demander_angle()
angle_radian = (angle_saisi * pi)/180
angle_minute = angle_saisi * 60
angle_seconde = angle_saisi * 3600
print(f"{angle_saisi} degrés = {angle_radian} radians")
print()
print(f"{angle_saisi} degrés = {angle_minute} minutes")
print()
print(f"{angle_saisi} degrés = {angle_seconde} secondes")
"""




# Exo 10 : Écrivez un programme qui calcule les intérêts accumulés chaque année pendant 20 ans, par capitalisation 
# d'une somme de 100 euros placée en banque au taux fixe de 4,3 %
"""
somme_initial = 100
somme_actuel = 100
i = 1
while i < 21:
    interet = somme_actuel * 0.43
    somme_actuel = somme_actuel + interet
    interet_accumulé = somme_actuel - somme_initial
    print(f"Pour l'année {i} l'interet accumulé est {interet_accumulé} FCFA et la valeur actuel est {somme_actuel} FCFA ")
    i = i+1
    ok = input("Appuyer sur entrer pour passer à l'année suivante")
"""

                    #------------------------------STRING--------------------------#

# COURS :  La séquence \n dans une chaîne provoque un saut à la ligne. • 
# La séquence \' permet d'insérer une apostrophe dans une chaîne délimitée par des apostrophes. De la même manière, 
# la séquence \" permet d'insérer des guillemets dans une chaîne délimitée elle-même par des guillemets. 

# EXO 11 : Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».
"""
mot = input("Saisissez un mot : ")
while mot != "":
    if 'e' in mot:
        print("Votre mot contient la lettre 'e' ") 
    else:
        print("Votre mot ne contient pas la lettre 'e' ")
    mot = input("Saisissez un autre mot : ")
"""

# EXO 11 : Écrivez un script qui compte le nombre d'occurrences du caractère « e » dans une chaîne.
"""
mot = input("Saisissez un mot : ")
while mot != "":
    nb_e = 0
    for i in range(0, len(mot)):
        if 'e' in mot[i] :
            nb_e = nb_e +1
         
    print(f"Le mot contient la lettre 'e' {nb_e} fois ")
    mot = input("Saisissez un autre mot : ")
"""


# EXO 11 : Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
#  Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »
"""
myVar = input("Saisissez une chaîne de caractère : ")
for i in range(0, len(myVar)):
    print(f"{myVar[i]}*",  end=" ")
"""



# EXO 11 : Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l'inversant. Ainsi par exemple, « zorglub » deviendra « bulgroz ».
"""
myVar = input("Saisissez une chaîne de caractère à cinq caractère : ")
while myVar != "":
    print(myVar[4], myVar[3], myVar[2], myVar[1], myVar[0])
    myVar = input("Saisissez une chaîne de caractère à cinq caractère : ")
"""

# EXO 12 : En partant de l'exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome 
# (c'est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».


#---------------------------------------- LISTES ----------------------------------------#
# EXO 13 : 
#Soient les listes suivantes :
#t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
#Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes en les alternant, 
# de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :
#['Janvier',31,'Février',28,'Mars',31, etc...].
"""
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = [t2[0], t1[0], t2[1], t1[1], t2[2], t1[2], t2[3], t1[3], t2[4], t1[4], t2[5], t1[5], t2[6], t1[6], t2[7], t1[7], t2[8], t1[8], t2[9], t1[9], t2[10], t1[10], t2[11], t1[11]]
print(t3)
"""




#EXO 14 : Écrivez un programme qui affiche « proprement » tous les éléments d'une liste. Si on l'appliquait par exemple à la liste t2 de l'exercice ci-dessus, on devrait obtenir :
#Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre Décembre
"""
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
for i in t2:
    print(i, end=" ")
"""





#EXO 15 : Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l'appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], 
# ce programme devrait afficher : le plus grand élément de cette liste a la valeur 75.
"""
print(" Ce programme va permettre d'identifier le plus grand nombre dans une liste de 5 nombre")
print()
liste = []
def demander_nbr(numéro):
    nbr = 0
    while nbr == 0:
        try:
            nbr_str = input(f"Veuillez saisir votre {numéro} nombre  : ")
            nbr = int(nbr_str)
            liste.append(nbr)
        except:
            print("Veuiller entrer un nombre  : ")
    return nbr
nbr1 = demander_nbr("premier")
nbr2 = demander_nbr("deuxième")
nbr3 = demander_nbr("troisième")
nbr4 = demander_nbr("quatrième")
nbr5 = demander_nbr("cinquième")

print(f"Le plus grand nombre est {max(liste)}")
"""





#EXO 16 : Écrivez un programme qui analyse un par un tous les éléments d'une liste de nombres (par exemple celle de l'exercice précédent) 
# pour générer deux nouvelles listes. L'une contiendra seulement les nombres pairs de la liste initiale, et l'autre les nombres impairs. 
# Par exemple, si la liste initiale est celle de l'exercice précédent, le programme devra construire une liste pairs qui contiendra [32, 12, 8, 2], 
# et une liste impairs qui contiendra [5, 3, 75, 15]. Astuce : pensez à utiliser l'opérateur modulo (%) déjà cité précédemment.
"""
print(" Ce programme va permettre d'identifier parmis une liste de 10 nombres, ceux qui sont pairs et ceux qui sont impairs")
print()
liste = []
def demander_nbr(numéro):
    nbr = 0
    while nbr == 0:
        try:
            nbr_str = input(f"Veuillez saisir votre {numéro} nombre  : ")
            nbr = int(nbr_str)
            liste.append(nbr)
        except:
            print("Veuiller entrer un nombre  : ")
    return nbr
nbr1 = demander_nbr("premier")
nbr2 = demander_nbr("deuxième")
nbr3 = demander_nbr("troisième")
nbr4 = demander_nbr("quatrième")
nbr5 = demander_nbr("cinquième")
nbr6 = demander_nbr("sixième")
nbr7 = demander_nbr("septième")
nbr8 = demander_nbr("huitième")
nbr9 = demander_nbr("neuvième")
nbr10 = demander_nbr("dixième")

liste_pair = []
liste_impair = []
for i in liste : 
    if i % 2 == 0 : 
        liste_pair.append(i)
    else:
        liste_impair.append(i)

print("Les nombres impairs sont : ", end=" ")
for i in liste_impair:
    print(i, end=" ")
print()

print("Les nombres pairs sont : ", end=" ")
for i in liste_pair:
    print(i, end=" ")
print()
"""



#EXO 17 : Écrivez un programme qui analyse un par un tous les éléments d'une liste de mots (par exemple :  ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'] )
# pour générer deux nouvelles listes. L'une contiendra les mots comportant moins de 6 caractères, l'autre les mots comportant 6 caractères ou davantage.
"""
liste = []
def demander_mot():
    mot = input("Veuillez entrer un mot (Cliquez sur entrer si vous n'avez plus de mot) : ")
    liste.append(mot)
    while mot != "":
        mot = input("Veuillez entrer un mot (Cliquez sur entrer si vous n'avez plus de mot) : ")
        liste.append(mot)
    
demander_mot()

moins_6_caractère = []
Plus_6_caractère = []
for i in liste:
    if len(i) < 6 :
        moins_6_caractère.append(i)
    else : 
        Plus_6_caractère.append(i)
print("Les mots de moins de six caractères sont : ", end=" ")
for i in moins_6_caractère:
    print(i, end=" ")
print()

print("Les mots de six caractères ou plus sont : ", end=" ")
for i in Plus_6_caractère:
    print(i, end=" ")
print()
"""





#EXO 18 : Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie par l'utilisateur 
# en miles/heure. (Rappel : 1 mile = 1609 mètres)
"""
print("Ce programme va convertir en mètres par seconde et en km/h une vitesse fournie par l'utilisateur en miles/heure ")
vitesse = 0
while vitesse == 0:
    try:
        vitesse_str = input("Veuillez entrer la vitesse que vous voulez convrtir : ")
        vitesse = int(vitesse_str)
    except:
        print("Veuiller entrer un nombre pour la vitesse")

print()
vitesse_km_h = vitesse * 1.609
vitesse_m_s = vitesse_km_h / 3.6

print(f"{vitesse} mile/heure correspond à {vitesse_km_h} km/h ou à {vitesse_m_s} m/s")
"""



#EXO 19 : Écrivez un programme qui calcule le périmètre et l'aire d'un triangle quelconque dont l'utilisateur fournit 
# les 3 côtés. (Rappel : l'aire d'un triangle quelconque se calcule à l'aide de la formule :
#dans laquelle d désigne la longueur du demi-périmètre, et a, b, c celles des trois côtés.)
"""
print("Calculons le périmètre et l'aire du triangle de votre choix")
def demander_nbr(numéro):
    nbr = 0
    while nbr == 0:
        try:
            nbr_str = input(f"Veuillez saisir la longueur du {numéro} côté  : ")
            nbr = int(nbr_str)
        except:
            print("Veuiller entrer un nombre  : ")
    return nbr
a = demander_nbr("premier")
b = demander_nbr("deuxième")
c = demander_nbr("troisième")

p = a + b + c
d = p / 2

aire = sqrt(d*(d-a)*(d-b)*(d-c))
print()
print(f"Le périmètre du triangle est {p} mètres")
print(f"L'aire du triangle est {a} mètre carrés")
"""



#EXO 20 : Écrivez un programme qui calcule la période d'un pendule simple de longueur donnée.
"""
print("Calculons ensemble le volume de votre pavé droit")
print()

longueur = 0
while longueur == 0:
    try:
        longueur_str = input("Entrer la longueur du pendule en mètre : ")
        longueur = int(longueur_str)
    except:
        print("Veuiller entrer un nombre pour la longueur")
print(f"Génial, Votre pendule à une longueur de {longueur} mètres. Passons à la prochaine étape!")
print()

période = 2*pi*sqrt(longueur/9.8)

print(f"La période du pendule est {période} secondes")
"""








                                        # ***COURS  ---  MODULE TURTLE***#

# Fonctions disponible avec le module turtules: reset() --> On efface tout et on recommence 
#                                               goto(x, y) --> Aller à l'endroit de coordonnées x, y 
#                                               forward(distance) --> Avancer d'une distance donnée 
#                                               backward(distance) --> Reculer 
#                                               up() --> Relever le crayon (pour pouvoir avancer sans dessiner) 
#                                               down() --> Abaisser le crayon (pour recommencer à dessiner) 
#                                               color(couleur) --> couleur peut être une chaîne prédéfinie ('red', 'blue', etc.) 
#                                               left(angle) --> Tourner à gauche d'un angle donné (exprimé en degrés) 
#                                               right(angle) --> Tourner à droite 
#                                               width(épaisseur) --> Choisir l'épaisseur du tracé 
#                                               fill(1) --> Remplir un contour fermé à l'aide de la couleur sélectionnée 
#                                               write(texte) --> texte doit être une chaîne de caractères


# TEST AVEC LE MODULE TURTLE
"""
a = 1
while a < 20 : 
    forward(100)
    left(60)
    forward(100)
    a = a+1
goto(5, 5)
"""


"""
a = 0 
if not a: 
    print('gagné') 
elif a: 
    print('perdu')
"""

# ----------------------------------------Mini programme----------------------------------------#


#EXO 21 : Reprendre le programme c) avec a = 0 au lieu de a = 1. Que se passe-t-il ? Conclure ! OK

#EXO 22 : Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres multiples de 3 
# et de 5 compris entre ces bornes. Prendre par exemple a = 0, b = 32 ; le résultat devrait être alors 0 + 15 + 30 = 45.
#  Modifier légèrement ce programme pour qu'il additionne les nombres multiples de 3 ou de 5 compris entre les bornes a et b. 
# Avec les bornes 0 et 32, le résultat devrait donc être : 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.
"""
print("Nous alons additionner les nombres multiples de 3 OU de 5 puis les nombres multiples de 3 ET de 5 entre deux bornes que vous choisirez")
def demander_nbr(numéro):
    nbr = 0
    while nbr == 0:
        try:
            nbr_str = input(f"Veuillez saisir votre {numéro} borne  : ")
            nbr = int(nbr_str)
        except:
            print("Veuiller entrer un nombre  : ")
    return nbr
nbr1 = demander_nbr("premiere")
nbr2 = demander_nbr("deuxième")

def addition_et():
    result1 = 0
    for i in range(nbr1, nbr2):
        if i%3 == 0 and i%5==0:
            result1 = result1 + i
    return result1


def addition_ou():
    result2 = 0
    for i in range(nbr1, nbr2):
        if i%3==0 or i%5==0:
            result2 = result2 + i
    return result2

total_et = addition_et()
total_ou = addition_ou()
print(f"La somme des nombres multiples de 3 ou de 5 entre {nbr1} et {nbr2} est : {total_ou} ")
print()
print(f"La somme des nombres multiples de 3 et de 5 entre {nbr1} et {nbr2} est : {total_et} ")
"""

#---------------------------------------- EXO SIMPLE ----------------------------------------#


#EXO 23 : Déterminer si une année (dont le millésime est introduit par l'utilisateur) est bissextile ou non. 
# Une année A est bissextile si A est divisible par 4. Elle ne l'est cependant pas si A est un multiple de 100,
#  à moins que A ne soit multiple de 400.   OK

#EXO 24 : Demander à l'utilisateur son nom et son sexe (M ou F). En fonction de ces données, afficher 
# « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne. OK

#EXO 28 : Soit la liste suivante : ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise'] 
# Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant. OK

#EXO 26 : Demander à l'utilisateur qu'il entre un nombre. Afficher ensuite : soit la racine carrée de ce nombre, 
# soit un message indiquant que la racine carrée de ce nombre ne peut être calculée. OK




#EXO 25 : Demander à l'utilisateur d'entrer trois longueurs a, b, c. À l'aide de ces trois longueurs, 
# déterminer s'il est possible de construire un triangle. Déterminer ensuite si ce triangle est rectangle, 
# isocèle, équilatéral ou quelconque. Attention : un triangle rectangle peut être isocèle.



#EXO 27 : Convertir une note scolaire N quelconque, entrée par l'utilisateur sous forme de points 
# (par exemple 27 sur 85), en une note standardisée suivant le code ci-dessous : 
# Note Appréciation N >= 80 % A 80 % > N >= 60 % B 60 % > N >= 50 % C 50 % > N >= 40 % D N < 40 % E
"""
note = 27
total_point = 85
N = (27 * 100) / total_point
if N >= 80:
    print("Bravo, vous avez un A")
elif 80 > N >= 60 :
    print("Bravo, vous avez un B")
elif 60 > N >= 50 :
    print("Bravo, vous avez un C")
elif 50 > N >= 40 :
    print("Bravo, vous avez un D")
else :
    print("Bravo, vous avez un E")
"""






#EXO 29 : Écrire une boucle de programme qui demande à l'utilisateur d'entrer des notes d'élèves. 
# La boucle se terminera seulement si l'utilisateur entre une valeur négative. Avec les notes ainsi entrées, 
# construire progressivement une liste. Après chaque entrée d'une nouvelle note (et donc à chaque itération de la boucle), 
# afficher le nombre de notes entrées, la note la plus élevée, la note la plus basse, la moyenne de toutes les notes.
"""
liste = []
def init():
    try:
        note_str = input(f"Veuillez saisir une note  : ")
        note = int(note_str)
        liste.append(note)
    except:
        print("Veuiller entrer une nombre")
        note_str = input(f"Veuillez saisir une note  : ")
        note = int(note_str)
        liste.append(note)
    return note

note = init()


while note >= 0:
    try:
        note_str = input(f"Veuillez saisir une note (Saisissez un nombre négatif pour arrêter)  : ")
        note = int(note_str)
        if note >= 0 :
            liste.append(note)
    except:
        print("Veuiller entrer une nombre")
print(liste)
print(f"Le nombre de note entré est {len(liste)}")
print(f"La note la plus forte est {max(liste)}")
print(f"La note la plus faible est {min(liste)}")
M = sum(liste) / len(liste)
print(f"La note la plus forte est {M}")
"""



#EXO 30 : Écrivez un script qui affiche la valeur de la force de gravitation s'exerçant entre deux masses de 10 000 kg ,
#  pour des distances qui augmentent suivant une progression géométrique de raison 2, à partir de 5 cm (0,05 mètre).
#La force de gravitation est régie par la formule 
#Exemple d'affichage : F = 6.67*10 E -11 (m*m'/d2)
#d = .05 m : la force vaut 2.668 N d = .1 m : la force vaut 0.667 N d = .2 m : la force vaut 0.167 N d = .4 m : la force vaut 0.0417 N
""""
print("Ce programme affiche la valeur de la force de gravitation s'exerçant entre deux masses de 10 000 kg , pour des distances qui augmentent suivant une progression géométrique de raison 2, à partir de 5 cm (0,05 mètre).")
d = 0.05
F = 6.67 * (10**-11) * (10**8)/(d**2)
c = 0

while c < 20:
    F = 6.67 * (10**-11) * (10**8)/(d**2)
    print(f"La force de gravitation s'exerçant entre deux masses de 10 000 kg séparées par une distance de {d} mètres est : {F} newton")
    d = d * 2
    c = c +1
"""


#EXO 25 : Demander à l'utilisateur d'entrer trois longueurs a, b, c. À l'aide de ces trois longueurs, 
# déterminer s'il est possible de construire un triangle. Déterminer ensuite si ce triangle est rectangle, 
# isocèle, équilatéral ou quelconque. Attention : un triangle rectangle peut être isocèle.




#---------------------------------------- FONCTIONS ----------------------------------------#
                                        #***COURS***#
# gloabal a --> Utiliser la variable global a dans une fonction
#__main__ --> Désigne le corps principal du program
#__doc__ --> Désigne le commentaire dans un objet (Attributs)
# Il est mieux de définir  les fonctions dans un autres fichier et de les importer dans le fichier principal
# Il est préferable d'affecter des valeurs par défaut aux paramètres d'une fonction lors de sa définition
# En affectant des valeurs par défauts aux paramètres, il n'est plus nécessaire de respecter un ordre dans l'attribution des arguments à la fonction lors de son appelation.

#ExO 31 : Importez le moduleturtle pour pouvoir effectuer des dessins simples.  SIMPLE


#ExO 32 : Vous allez dessiner une série de triangles équilatéraux de différentes couleurs. Pour ce faire, définissez d'abord une 
# fonction triangle() capable de dessiner un triangle d'une couleur bien déterminée (ce qui signifie donc que la définition de 
# votre fonction doit comporter un paramètre pour recevoir le nom de cette couleur). Utilisez ensuite cette fonction pour 
# reproduire ce même triangle en différents endroits, en changeant de couleur à chaque fois.
""""
def triangle(couleur, x, y):
    up()
    goto(x, y)
    down()
    c = 0
    while c <3:
        color(couleur)
        forward(50)
        right(120)
        c = c + 1
    
    
triangle("red", 0, 0)
triangle("blue", 100, 100)
triangle("green", 200, 200)
triangle("yellow", -200, -200)

exitonclick()

"""



#ExO 33 : Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca.
"""
def ligneCar(n, ca):
    chaine = []
    c = 1 
    while c <=n :
        chaine.append(ca)
        c = c + 1
    print(chaine)
ligneCar(3, "Cool")
print("ok")
"""

        

#ExO 34 : [SIMPLE] Définissez une fonction surfCercle(R). Cette fonction doit renvoyer la surface (l'aire) d'un cercle dont on lui a fourni le rayon R en argument. 
# Par exemple, l'exécution de l'instruction : print(surfCercle(2.5))  doit donner le résultat : 19.63495...




#ExO 35 : [SIMPLE] Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d'une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments. 
# Par exemple, l'exécution de l'instruction : print(volBoite(5.2, 7.7, 3.3))  doit donner le résultat : 132.132.



#ExO 36 : Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres n1, n2, n3 fournis en arguments. 
# Par exemple, l'exécution de l'instruction : print(maximum(2,5,4))  doit donner le résultat : 5.
""""
print(" Ce programme va permettre d'identifier parmis une liste de 3 nombres, lequel est le plus grand")
print()
liste = []
def demander_nbr(numero):
    nbr = 0
    while nbr == 0:
        try:
            nbr_str = input(f"Veuillez saisir votre {numero} nombre  : ")
            nbr = int(nbr_str)
            liste.append(nbr)
        except:
            print("Veuiller entrer un nombre  : ")
    return nbr
nbr1 = demander_nbr("premier")
nbr2 = demander_nbr("deuxieme")
nbr3 = demander_nbr("troisieme")

def maximun (x, y, z) : 
    result = max(liste)
    print(f"Le nombre le plus grand est : {result} ")

maximun(nbr1, nbr2, nbr3)
"""




#ExO 37 : Complétez le module de fonctions graphiques dessins_tortue.py décrit à la page . Commencez par ajouter un paramètre angle à la fonction carre(), de manière à ce que 
# les carrés puissent être tracés dans différentes orientations. Définissez ensuite une fonction triangle(taille, couleur, angle) capable de dessiner un triangle équilatéral 
# d'une taille, d'une couleur et d'une orientation bien déterminées. Testez votre module à l'aide d'un programme qui fera appel à ces fonctions à plusieurs reprises, avec 
# des arguments variés pour dessiner une série de carrés et de triangles : (VOIR IMAGE)
"""
position = -300
up()
goto(-300, 100)
down()
def carree(taille, couleur, orientation):
    c = 0
    while c < 4:
        color(couleur)
        forward(taille)
        right(orientation)
        c = c +1
    global position
    position = position + taille + 10
    up()
    goto(position, 100)
    down()

def triangle(taille2, couleur2):
    c2 = 0
    while c2 <3:
        color(couleur2)
        forward(50)
        right(120)
        c2 = c2 + 1
    global position
    position = position + taille2 + 10
    up()
    goto(position, 100)
    down()

carree(100, "red", 90)
triangle(50, "green")
carree(100, "blue", 90)
triangle(50, "yellow")
carree(100, "grey", 90)
triangle(50, "cyan")
carree(100, "orange", 90)
triangle(50, "violet")

exitonclick()
"""





#ExO 38 : Ajoutez au module de l'exercice précédent une fonction etoile5() spécialisée dans le dessin d'étoiles à 5 branches. Dans votre programme principal, 
# insérez une boucle qui dessine une rangée horizontale de de 9 petites étoiles de tailles variées : (VOIR IMAGE)
# position = -300
# up()
# goto(-300, 100)
# down()
# def etoile5(couleur):
#                       DESSIN DESSIN DESSIN
    



#ExO 39 : Ajoutez au module de l'exercice précédent une fonction etoile6() capable de dessiner une étoile à 6 branches, elle- même constituée de deux triangles équilatéraux 
# imbriqués. Cette nouvelle fonction devra faire appel à la fonction triangle() définie précédemment.  (VOIR IMAGE)
#                       DESSIN DESSIN DESSIN




#ExO 40 : Définissez une fonction indexMax(liste) qui renvoie l'index de l'élément ayant la valeur la plus élevée dans la liste transmise en argument. 
# Exemple d'utilisation : serie = [5, 8, 2, 1, 9, 3, 6, 7] print(indexMax(serie)) 4
"""
def indexMax (liste):
    result = max(liste)
    index = indexOf(liste, result)
    return index

print(indexMax([5, 8, 2, 1, 9, 3, 6, 7]))
"""


#ExO 41 : Définissez une fonction nomMois(n) qui renvoie le nom du n-ième mois de l'année. Par exemple, l'exécution de l'instruction : print(nomMois(4)) doit donner le résultat : Avril.
"""
def nomMois(n):
    baseDeDonnees = { "1" : "Janvier",
                      "2" : "Février",
                      "3" : "Mars",
                      "4" : "Avril",
                      "5" : "Mai",
                      "6" : "Juin",
                      "7" : "Juillet",
                      "8" : "Aout",
                      "9" : "Septembre",
                      "10" : "Octobre",
                      "11" : "Novembre",
                      "12" : "Decembre"}
    for i in range(1, 25):
        if n == i:
            i_str = str(i)
            print(f"Votre nombre correspond à : {baseDeDonnees[i_str]} ")
nomMois(12)
"""    
            
    


#ExO 42 : Définissez une fonction inverse(ch) qui permette d'inverser les l'ordre des caractères d'une chaîne quelconque. La chaîne inversée sera renvoyée au programme appelant.
# REFLEXION  REFLEXION  REFLEXION
# liste = ["cool", "john"]
# liste.reverse()
# print(liste)
#join(reversed("cool"))



#ExO 43 : Définissez une fonction compteMots(ph) qui renvoie le nombre de mots contenus dans la phrase ph. On considère comme mots les ensembles de caractères inclus 
# entre des espaces.
"""
def comptesMots(ph):
    compteur = 0
    for i in ph:
        if i == " " :
            compteur = compteur + 1
        elif i =="'":
            compteur = compteur + 1
    print(f"Votre phrase compte {compteur + 1} mots")

phrase = input("Veuillez saisir votre phrase : ")
comptesMots(phrase)
"""






#ExO 44 :[SIMPLE] Modifiez la fonction volBoite(x1,x2,x3) que vous avez définie dans un exercice précédent, de manière à ce qu'elle puisse être appelée avec trois, deux, un seul, 
# ou même aucun argument. Utilisez pour ceux ci des valeurs par défaut égales à 10. Par exemple : print(volBoite())doit donner le résultat : 1000 print(volBoite(5.2))doit 
# donner le résultat : 520.0 print(volBoite(5.2, 3))doit donner le résultat : 156.0




#ExO 45 : Modifiez la fonction volBoite(x1,x2,x3) ci-dessus de manière à ce qu'elle puisse être appelée avec un, deux, ou trois arguments. Si un seul est utilisé, la boîte est 
# considérée comme cubique (l'argument étant l'arête de ce cube). Si deux sont utilisés, la boîte est considérée comme un prisme à base carrée (auquel cas le premier argument 
# est le côté du carré, et le second la hauteur du prisme). Si trois arguments sont utilisés, la boîte est considérée comme un parallélépipède. Par exemple : print(volBoite())doit 
# donner le résultat : -1 (indication d'une erreur) print(volBoite(5.2))doit donner le résultat : 140.608 print(volBoite(5.2, 3))doit donner le résultat :
#  81.12 print(volBoite(5.2, 3, 7.4))doit donner le résultat : 115.44
"""
def volBoite(x1=0, x2=0, x3=0):
    if x2==0 and x3==0:
        volume = x1**3
        print(f"Le volume de votre cube est : {volume} ")
    elif x3==0:
        volume = (x1**2) * x2
        print(f"Le volume de votre prisme à base carree est : {volume} ")
    else:
        volume = x1*x2*x3
        print(f"Le volume de votre parallélépipède est : {volume} ")
        
volBoite(5)
volBoite(2,3)
volBoite(6,4,2)
"""
    



#ExO 46 : Définissez une fonction changeCar(ch,ca1,ca2,debut,fin) qui remplace tous les caractères ca1 par des caractères ca2 dans la chaîne de caractères ch, à partir de
#  l'indice debut et jusqu'à l'indice fin, ces deux derniers arguments pouvant être omis (et dans ce cas la chaîne est traitée d'une extrémité à l'autre). 
# Exemples de la fonctionnalité attendue :
#>>> phrase = 'Ceci est une toute petite phrase.' 
# >>> print(changeCar(phrase, '', '*')) Ceci*est*une*toute*petite*phrase. 
# >>> print(changeCar(phrase, '', '*', 8, 12)) Ceci est*une*toute petite phrase. 
# >>> print(changeCar(phrase, '', '*', 12)) Ceci est une*toute*petite*phrase. 
# >>> print(changeCar(phrase, '', '*', fin = 12)) Ceci*est*une*toute petite phrase.
"""
REFLEXION  REFLEXION REFLEXION
def changeCar(ch,ca1,ca2,debut=0,fin=0):
    if debut!=0 and fin!=0:
        for i in range(debut, fin):
            if ch[i]==ca1:
                newCh = ch.replace(ca1, ca2)
        print(newCh)
    elif debut==0 or fin==0:
        for i in range(0, len(ch)):
            if ch[i]==ca1:
                newCh = ch.replace(ca1, ca2)
        print(newCh)
changeCar("C'est vraiment cool de coder en python", "e","*", 0, 10)
changeCar("C'est vraiment cool de coder en python", "e","*", 2, 10)
"""

#ExO 47 : Définissez une fonction eleMax(liste,debut,fin) qui renvoie l'élément ayant la plus grande valeur dans la liste transmise. 
# Les deux arguments debut et fin indiqueront les indices entre lesquels doit s'exercer la recherche, et chacun d'eux pourra être omis (comme dans l'exercice précédent). 
# Exemples de la fonctionnalité attendue :
#>>> serie = [9, 3, 6, 1, 7, 5, 4, 8, 2] 
# >>> print(eleMax(serie)) 9 
# >>> print(eleMax(serie, 2, 5)) 7 
# >>> print(eleMax(serie, 2)) 8 
# >>> print(eleMax(serie, fin =3, debut =1)) 6


#----------------------------------------UTILISATION DE FENETRES ET DE GRAPHISME----------------------------------------#
# COURS :
# *GUI --> Graphic User Interface
# *OOP --> Object orienred Programming
# * CLARIFICATION --> Chaque système d'exploitation peut en effet proposer
# plusieurs « bibliothèques » de fonctions graphiques de base, auxquelles viennent fréquemment s'ajouter de nombreux
# compléments, plus ou moins spécifiques de langages de programmation particuliers. Tous ces composants sont
# généralement présentés comme des classes d'objets, dont il vous faudra étudier les attributs et les méthodes.

# EVENEMENTS --> . Il existe un grand nombre de ces événements (mouvements et clics de la souris, enfoncement
#des touches du clavier, positionnement et redimensionnement des fenêtres, passage au premier plan, etc.).
# Voir ouvrages de référence de Tkinter

# SYNTAXE --> la syntaxe des instructions destinées à mettre en œuvre une méthode associée à un objet :
# objet.méthode(arguments)

# EVENT() -->  permet de transmettre au gestionnaire d'événement un certain nombre d'attributs de l'événement :
# le type de l'évenement - Une série d'attribut de l'évenement

# 15 CLASSES de base pour les widgets tkinter --> Canvas - Button - Entry - Frame - Menu - Checkbutton - Toplevel - Scrollbar
# Scale - Text - Listbox - Message - Menubutton - Radiobutton - Label [VOIR DOCUMENTATION TKINTER]

# POSITIONEMENT DES WIDGETS --> Methodes grid()  -  place()  -  pack()  





# CodeCours1
"""
fen1 = Tk() # Création d'une instance de l'objet fenêtre
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red') # Instanciation du module Label()
tex1.pack()         # Sert à l'encapsulation de l'objet et l'adaptation de la géométrie de la fenêtre
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)  # Instanciation du module Label()
bou1.pack()         # Sert à l'encapsulation de l'objet et l'adaptation de la géométrie de la fenêtre
fen1.mainloop()   # Lance le programme en re rendant réceptifs au différents évenements (Clavier, souris etc...)
"""

#** PROGRAMMES PILOTES PAS DES EVENEMENTS
# Structure d'un programme classique --> Initialisation - Centrale - Terminaison
# Structure d'un programme pilotes par des evenements --> Initialisation - Reception + Traitemenst d'évenement - Terminaison



# CodeCours2
"""
# Petit exercice utilisant la bibliothèque graphique tkinter
from random import randrange
# --- définition des fonctions gestionnaires d'événements : ---#
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1-10

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]
    
    
#------ Programme principal -------#
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 190, 190, 10   # coordonnées de la ligne
coul = 'dark green'                 # couleur de la ligne

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
fen1.mainloop() # démarrage du réceptionnaire d'événements
fen1.destroy() # destruction (fermeture) de la fenêtre
"""


#***EXERCICES
#Exo 47 : Comment faut-il modifier le programme pour ne plus avoir que des lignes de couleur cyan, maroon et green ?
"""
En les supprimant de la liste  :   pal=['purple','cyan','maroon','green','red','blue','orange','yellow']

"""

#Exo 48 :  Comment modifier le programme pour que toutes les lignes tracées soient horizontales et parallèles ?
"""
IL FAUT DONNER LES MEMES ORDONNEES AU DEUX POINTS DE CHAQUE DROITE. IL FAUT AUSSI LES FAIRE SUBIR LES 
MEMES VARIATIONS

def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1+10

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]
    
    
#------ Programme principal -------#
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 10, 190, 10   # coordonnées de la ligne
coul = 'dark green'                 # couleur de la ligne

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
fen1.mainloop() # démarrage du réceptionnaire d'événements
fen1.destroy() # destruction (fermeture) de la fenêtre
"""

#Exo 49 : [SIMPLE] .Agrandissez le canevas de manière à lui donner une largeur de 500 unités et une hauteur de 650. Modifiez également
# la taille des lignes, afin que leurs extrémités se confondent avec les bords du canevas.


#Exo 50 :  .Ajoutez une fonction drawline2 qui tracera deux lignes rouges en croix au centre du canevas : l'une horizontale et
# l'autre verticale. Ajoutez également un bouton portant l'indication « viseur ». Un clic sur ce bouton devra provoquer
# l'affichage de la croix.
"""
def drawline2():
    "Tracé d'une ligne dans le canevas can1"
    global coul
    x1, y1, x2, y2 = 10, 100, 190, 100
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    x1, y1, x2, y2 = x1+90, y1-90, x2-90, y2+90
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    
    # modification des coordonnées pour la croix suivante : !!!
    
    

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]
    
    
#------ Programme principal -------#
# les variables suivantes seront utilisées de manière globale :
  # coordonnées de la ligne
coul = 'dark green'                 # couleur de la ligne

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
# bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
# bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
bou4 = Button(fen1,text='Viseur',command=drawline2)
bou4.pack(side=RIGHT)
fen1.mainloop() # démarrage du réceptionnaire d'événements
fen1.destroy() # destruction (fermeture) de la fenêtre
"""

# Exo 51 : .Reprenez le programme initial. Remplacez la méthode create_line par create_rectangle. Que se passe-t-il ?
# De la même façon, essayez aussi create_arc, create_oval, et create_polygon.
# Pour chacune de ces méthodes, notez ce qu'indiquent les coordonnées fournies en paramètres.
# (Remarque : pour le polygone, il est nécessaire de modifier légèrement le programme !)
"""
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    #can1.create_rectangle(x1,y1,x2,y2,width=2,fill=coul)
    #can1.create_arc(x1,y1,x2,y2,width=2,fill=coul)
    #can1.create_oval(x1,y1,x2,y2,width=2,fill=coul)
    can1.create_polygon(x1,y1,x2,y2,width=10,fill=coul)
    
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1-10

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]
    
    
#------ Programme principal -------#
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 190, 190, 10   # coordonnées de la ligne
coul = 'dark green'                 # couleur de la ligne

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=300,width=300)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
fen1.mainloop() # démarrage du réceptionnaire d'événements
fen1.destroy() # destruction (fermeture) de la fenêtre
"""

# Exo 52 : [SIMPLE] .- Supprimez la ligne global x1, y1, x2, y2 dans la fonction drawline du programme original. Que se passe-t-il ?
# Pourquoi ?
# - Si vous placez plutôt « x1, y1, x2, y2 » entre les parenthèses, dans la ligne de définition de la fonction drawline,
# de manière à transmettre ces variables à la fonction en tant que paramètres, le programme fonctionne-t-il encore ?
# N'oubliez pas de modifier aussi la ligne du programme qui fait appel à cette fonction !
# - Si vous définissez x1, y1, x2, y2 = 10, 390, 390, 10 à la place de global x1, y1, ..., que se passe-t-il ? Pourquoi ?
# Quelle conclusion pouvez-vous tirer de tout cela ?


# Exo 53 : .a) Créez un court programme qui dessinera les 5 anneaux olympiques dans un rectangle de fond blanc (white). Un
# bouton « Quitter » doit permettre de fermer la fenêtre.
"""
myFen = Tk()
myCanvas = Canvas(myFen, bg="white", width=400, height=400)
myCanvas.pack(side=LEFT)
btn = Button(myFen, text="Quitter", command=myFen.destroy)
btn.pack()
myCanvas.create_oval(20, 380, 380, 20, width=2, fill="blue")
myCanvas.create_oval(40, 360, 360, 40, width=2, fill="green")
myCanvas.create_oval(60, 340, 340, 60, width=2, fill="violet")
myCanvas.create_oval(80, 320, 320, 80, width=2, fill="red")
myCanvas.create_oval(100, 300, 300, 100, width=2, fill="blue")
myFen.mainloop()
"""


# b) Modifiez le programme ci-dessus en y ajoutant 5 boutons. Chacun de ces boutons provoquera le tracé de chacun
# des 5 anneaux
"""
# Mes fonction dessinateur
def anneau1():
    myCanvas.create_oval(20, 380, 380, 20, width=2, fill="blue")
    
def anneau2():
    myCanvas.create_oval(40, 360, 360, 40, width=2, fill="green")
    
def anneau3():
    myCanvas.create_oval(60, 340, 340, 60, width=2, fill="violet")

def anneau4():
    myCanvas.create_oval(80, 320, 320, 80, width=2, fill="red")

def anneau5():
    myCanvas.create_oval(100, 300, 300, 100, width=2, fill="blue")
    
    
myFen = Tk()
myCanvas = Canvas(myFen, bg="white", width=400, height=400)
myCanvas.pack(side=LEFT)
# Bouton pour dessiner les anneaux
btn1 = Button(myFen, text="Anneau 1", command=anneau1)
btn1.pack()

btn2 = Button(myFen, text="Anneau 2", command=anneau2)
btn2.pack()

btn3 = Button(myFen, text="Anneau 3", command=anneau3)
btn3.pack()

btn4 = Button(myFen, text="Anneau 4", command=anneau4)
btn4.pack()

btn5 = Button(myFen, text="Anneau 5", command=anneau5)
btn5.pack()
# Bouton pour quitter
btn = Button(myFen, text="Quitter", command=myFen.destroy)
btn.pack()

myFen.mainloop()
"""
# Exo 54 : [NOTES] .Dans votre cahier de notes, établissez un tableau à deux colonnes. Vous y noterez à gauche les définitions des
# classes d'objets déjà rencontrées (avec leur liste de paramètres), et à droite les méthodes associées à ces classes
# (également avec leurs paramètres). Laissez de la place pour compléter ultérieurement.

# CodeCours3
"""
def cercle(x, y, r, coul ='black'):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, outline=coul)
    
def figure_1():
    "dessiner une cible"
    can.delete(ALL) # Effacer d'abord tout dessin préexistant :
    # tracer les deux lignes (vert. Et horiz.) :
    can.create_line(100, 0, 100, 200, fill ='blue')
    can.create_line(0, 100, 200, 100, fill ='blue')
    # tracer plusieurs cercles concentriques :
    rayon = 15
    while rayon < 100:
        cercle(100, 100, rayon)
        rayon += 15
        
def figure_2():
    "dessiner un visage simplifié"
    # Effacer d'abord tout dessin préexistant :
    can.delete(ALL)
    # Les caractéristiques de chaque cercle sont
    # placées dans une liste de listes :
    cc =[[100, 100, 80, 'red'], # visage
    [70, 70, 15, 'blue'], # yeux
    [130, 70, 15, 'blue'], 
    [70, 70, 5, 'black'], 
    [130, 70, 5, 'black'],
    [44, 115, 20, 'red'], # joues
    [156, 115, 20, 'red'],
    [100, 95, 15, 'purple'], # nez
    [100, 145, 30, 'purple']] # bouche
    # on trace tous les cercles à l'aide d'une boucle :
    i =0
    while i < len(cc): # parcours de la liste
        el = cc[i] # chaque élément est lui-même une liste
        cercle(el[0], el[1], el[2], el[3])
        i += 1
##### Programme principal : ############
fen = Tk()
can = Canvas(fen, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='dessin 1', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='dessin 2', command =figure_2)
b2.pack(side =RIGHT, padx =3, pady =3)
fen.mainloop()
"""

# Exo 55  : .Inspirez-vous du script précédent pour écrire une petite application qui fait apparaître un damier 
# (dessin de cases noires sur fond blanc) lorsque l'on clique sur un bouton ajoutez un bouton qui fera apparaître 
# des pions au hasard sur le damier (chaque pression sur le bouton fera apparaître un nouveau pion).
"""
def line1(lineHeight):
    x1, y1, x2, y2 = 0, lineHeight, 50, lineHeight + 50
    for _ in range(5):
        myCanvas.create_rectangle(x1, y1, x2, y2, width=1, fill="dark blue")
        x1 += 100
        x2 += 100
        
def line2(lineHeight):
    x1, y1, x2, y2 = 50, lineHeight, 100, lineHeight + 50
    for _ in range(5):
        myCanvas.create_rectangle(x1, y1, x2, y2, width=1, fill="dark blue")
        x1 += 100
        x2 += 100

def drawBoard(numLine = 0):
    for _ in range(5):
        line1(numLine)
        numLine+=50
        line2(numLine)
        numLine+=50
def listCenter():   # sourcery skip: avoid-builtin-shadow
    x = 25
    list = [x]
    for _ in range(9):
        x += 50
        list.append(x)
    return list


# def listY():   # sourcery skip: avoid-builtin-shadow
#     y = 25
#     list = [y]
#     for _ in range(9):
#         y += 50
#         list.append(y)
#     return list

def drawPawn():
    x = choice(list)
    y = choice(list)
    cercle(x,y)

    
def cercle(x, y, r=20):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    myCanvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
        
# Création de la fenêtre et du canvas
# sourcery skip: avoid-builtin-shadow
myFen = Tk()
myCanvas = Canvas(myFen, bg="white", width=500, height=500)
myCanvas.pack(side=TOP, padx=5, pady=5)

# Création des boutons

btn = Button(myFen, text="DAMIER", command=drawBoard)
btn.pack(side =LEFT, padx =3, pady =3)

btn2 = Button(myFen, text="PIONS", command=drawPawn)
btn2.pack(side =RIGHT, padx =3, pady =3)

# Liste des centres de pions possibles

list = listCenter()
# c = 0
# while c <1000:
#     drawPawn()
#     c+=1
#     delay(10000000)

myFen.mainloop()

"""

#CodeCours4 : Calculatrice
"""
# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
def evaluer(event):
 chaine.configure(text=f"Resultat = {str(eval(entree.get()))}") # get() --> Extraction du contenu de entree
                                                                # eval() --> Evaluation
# ----- Programme principal : -----
fenetre = Tk()
entree = Entry(fenetre)  # Création de la zone pour recevoir le formules saisies par l'utilisateur
entree.bind("<Return>", evaluer) #Lier l'événement <pression sur la touche Return> à l'objet <entree>, 
                                        #le gestionnaire de cet événement étant la fonction <evaluer> 
chaine = Label(fenetre)  # Création de la chaine à configurer pour afficher le résultat de l'opération
entree.pack()
chaine.pack()
fenetre.mainloop()
"""
# CodeCours 5 :  détection et positionnement d'un clic souris
"""
# Détection et positionnement d'un clic de souris dans une fenêtre :
def pointeur(event):
    chaine.configure(text=f"Clic detecte en X ={str(event.x)}, Y ={str(event.y)}")
fen = Tk()
cadre = Frame(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()
"""

# Exo 55  : .Modifiez le script ci-dessus de manière à faire apparaître un petit cercle rouge à l'endroit où l'utilisateur a effectué
# son clic (vous devrez d'abord remplacer le widget Frame par un widget Canvas).
"""
def pointeur(event):
    chaine.configure(text=f"Clic detecte en X ={str(event.x)}, Y ={str(event.y)}")
    cercle(event.x, event.y)
    
def cercle(x, y, r=10):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    cadre.create_oval(x-r, y-r, x+r, y+r, fill="red")
    
fen = Tk()
cadre = Canvas(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()
"""

# CodeCours 6 :  Positionement de widgets
"""
fen1 = Tk()
txt1 = Label(fen1, text = 'Premier champ :')
txt2 = Label(fen1, text = 'Second :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
txt1.grid(row =0, sticky =E)
txt2.grid(row =1, sticky =E)
entr1.grid(row =0, column =1)
entr2.grid(row =1, column =1)
fen1.mainloop()
"""
"""
fen1 = Tk()
# création de widgets 'Label' et 'Entry' :
txt1 = Label(fen1, text ='Premier champ :')
txt2 = Label(fen1, text ='Second :')
txt3 = Label(fen1, text ='Troisième :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)
# création d'un widget 'Canvas' contenant une image bitmap :
can1 = Canvas(fen1, width =160, height =160, bg ='white')
photo = PhotoImage(file ='im.gif')
item = can1.create_image(80, 80, image =photo)
# Mise en page à l'aide de la méthode 'grid' :
txt1.grid(row =1, sticky =E)
txt2.grid(row =2, sticky =E)
txt3.grid(row =3, sticky =E)
entr1.grid(row =1, column =2)
entr2.grid(row =2, column =2)
entr3.grid(row =3, column =2)
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)
# démarrage :
fen1.mainloop()
"""

# CodeCours 7 :  Déplacement d'objet
"""
# procédure générale de déplacement :
def avance(gd, hb):
    global x1, y1
    x1, y1 = x1 +gd, y1 +hb
    can1.coords(oval1, x1,y1, x1+30,y1+30)
# gestionnaires d'événements :
def depl_gauche():
    avance(-10, 0)
def depl_droite():
    avance(10, 0)
def depl_haut():
    avance(0, -10)
def depl_bas():
    avance(0, 10) 
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 # coordonnées initiales
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=300,width=300)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.pack(side=LEFT)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
Button(fen1,text='Gauche',command=depl_gauche).pack()
Button(fen1,text='Droite',command=depl_droite).pack()
Button(fen1,text='Haut',command=depl_haut).pack()
Button(fen1,text='Bas',command=depl_bas).pack()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()
"""

# Exercices
#  Exo 55  : .Écrivez un programme qui fait apparaître une fenêtre avec un canevas. Dans ce canevas on verra deux cercles
# (de tailles et de couleurs différentes), qui sont censés représenter deux astres. Des boutons doivent permettre de
# les déplacer à volonté tous les deux dans toutes les directions. Sous le canevas, le programme doit afficher en
# permanence : a) la distance séparant les deux astres; b) la force gravitationnelle qu'ils exercent l'un sur l'autre (penser
# à afficher en haut de fenêtre les masses choisies pour chacun d'eux, ainsi que l'échelle des distances). Dans cet
# exercice, vous utiliserez évidemment la loi de la gravitation universelle de Newton (cf. exercice 6.16, page , et un
# manuel de Physique générale).


#  Exo 56 : .En vous inspirant du programme qui détecte les clics de souris dans un canevas, modifiez le programme ci-dessus
# pour y réduire le nombre de boutons : pour déplacer un astre, il suffira de le choisir avec un bouton, et ensuite de
# cliquer sur le canevas pour que cet astre se positionne à l'endroit où l'on a cliqué.


#  Exo 57  : .Extension du programme ci-dessus. Faire apparaître un troisième astre, et afficher en permanence la force résultante
# agissant sur chacun des trois (en effet : chacun subit en permanence l'attraction gravitationnelle exercée par les
# deux autres !).


#  Exo 58  : .Même exercice avec des charges électriques (loi de Coulomb). Donner cette fois une possibilité de choisir le signe
# des charges.


#  Exo 59  : .Écrivez un petit programme qui fait apparaître une fenêtre avec deux champs : l'un indique une température en
# degrés Celsius, et l'autre la même température exprimée en degrés Fahrenheit. Chaque fois que l'on change une
# quelconque des deux températures, l'autre est corrigée en conséquence. Pour convertir les degrés Fahrenheit en
# Celsius et vice-versa, on utilise la formule . Revoyez aussi le petit programme concernant la
# calculatrice simplifiée (page ).


#  Exo 60  : .Écrivez un programme qui fait apparaître une fenêtre avec un canevas. Dans ce canevas, placez un petit cercle
# censé représenter une balle. Sous le canevas, placez un bouton. Chaque fois que l'on clique sur le bouton, la balle
# doit avancer d'une petite distance vers la droite, jusqu'à ce qu'elle atteigne l'extrémité du canevas. Si l'on continue à
# cliquer, la balle doit alors revenir en arrière jusqu'à l'autre extrémité, et ainsi de suite.


#  Exo 61  : .Améliorez le programme ci-dessus pour que la balle décrive cette fois une trajectoire circulaire ou elliptique dans le
# canevas (lorsque l'on clique continuellement). Note : pour arriver au résultat escompté, vous devrez nécessairement
# définir une variable qui représentera l'angle décrit, et utiliser les fonctions sinus et cosinus pour positionner la balle
# en fonction de cet angle.


# Exo 62  :  .Modifiez le programme ci-dessus de telle manière que la balle, en se déplaçant, laisse derrière elle une trace de
# la trajectoire décrite.


# Exo 63  : .Modifiez le programme ci-dessus de manière à tracer d'autres figures. Consultez votre professeur pour des
# suggestions (courbes de Lissajous).


# Exo 64  :  .Écrivez un programme qui fait apparaître une fenêtre avec un canevas et un bouton. Dans le canevas, tracez
# un rectangle gris foncé, lequel représentera une route, et par-dessus, une série de rectangles jaunes censés
# représenter un passage pour piétons. Ajoutez quatre cercles colorés pour figurer les feux de circulation concernant
# les piétons et les véhicules. Chaque utilisation du bouton devra provoquer le changement de couleur des feux : (VOIR IMAGE)


# Exo 65  :  .Écrivez un programme qui montre un canevas dans lequel est dessiné un circuit électrique simple (générateur +
# interrupteur + résistance). La fenêtre doit être pourvue de champs d ' entrée qui permettront de paramétrer chaque
# élément (c ' est-à-dire choisir les valeurs des résistances et tensions). L ' interrupteur doit être fonctionnel (prévoyez
# un bouton « Marche/arrêt » pour cela). Des « étiquettes » doivent afficher en permanence les tensions et intensités
# résultant des choix effectués par l ' utilisateur.
