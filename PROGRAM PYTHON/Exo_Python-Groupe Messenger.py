
def demander_nbr():
    nbr = 0
    while nbr == 0:
        try:
            nbr_str = input("Veuillez entrer un nombre : ")
            nbr = int(nbr_str)
        except Exception:
            print("Vous n'avez pas saisi un nombre!!  VEUILLEZ REESSAYER")
    return nbr

def confirmation():   # CONTINUER OU NON  A ENTRER DES NOMBRES
    # sourcery skip: merge-comparisons, merge-duplicate-blocks, remove-redundant-if
    condition = 0
    while condition ==0 :
        confirm = input("Entrer oui pour continuer et non pour arreter : ")
        if confirm == "oui":
            condition = 1
        elif confirm == "non":
            condition = 1
        else:
            print("VEUILLEZ ENTRER oui OU non SVP!!!")
            condition = 0
    return confirm   
    
      

def lancement():   # POUR LANCER LE PROGRAMME ET RECCUEULLIR LA LISTE DESORDONNEE DE L'UTILISATEUR
    liste = []
    confirm = "oui"
    while confirm == "oui" :
        valeur = demander_nbr()
        liste.append(valeur)
        confirm = confirmation()
    print()
    print("FELICITATIONS, voila la liste que vous avez constituer : ", end=" ")
    for i in liste : 
        print (i, end=" ")
    return liste
        
def demanderOrdre():   # POUR DEMANDER L'ORDRE DE RANGEMENT
    condition = 0
    while condition ==0:
        ordre = input("""Dans quel ordre voulez vous ranger vos nombre??
                        Si c'est l'ordre croissant entrer : c 
                        Si c'est l'ordre decroissant entrer : d
                        Si vouv voulez les deux entrer : les2
                        
                        VOTRE REPONSE : """)
        if ordre in ["c", "d", "les2"]:
            condition = 1
        else:
            print("VEUILLEZ ENTRER oui OU non SVP!!!")
            condition = 0
    return ordre  

def ordreCroissant():  # POUR RANGER DANS L'ORDRE CROISSANT
    liste.sort(reverse=True)
    print("FELICITATIONS, voila vos nombres rangés dans l'ordre croissant : ", end=" ")
    for i in liste : 
        print (i, end=" ")
        
def ordreDecroissant():   # POUR RANGER DANS L'ORDRE DECROISSANT
    liste.sort(reverse=False)
    print("FELICITATIONS, voila vos nombres rangés dans l'ordre decroissant  : ", end=" ")
    for i in liste : 
        print (i, end=" ")
    
    
def classement():  # POUR AFFICHER LE CLASSEMENT SELON LE CHOIX
    global ordre
    if ordre == "c":
        ordreCroissant()
    elif ordre == "d":
        ordreDecroissant
    elif ordre == "les2":
        ordreCroissant()
        print()
        ordreDecroissant()
        
    

#---PROGRAMME PRINCIPAL---#
print("""      BIENVENUE DANS MON PROGRAMME    
            JE VAIS VOUS AIDER A RANGER DANS L'ORDRE DE VOTRE CHOIX DES NOMBRES QUE VOUS ALLER RENTRER EN DESODRE
               ALORS, C'EST PARTI!!!""")
liste = lancement()
print()
print()
ordre = demanderOrdre()
print()
classement()


