
# Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
# Refaire la saisie du nom, mais avec l’instruction raw_input(). L’afficher.
# Enfin, utilisez la « bonne pratique » : recommencez l’exercice en transtypant les saisies
# effectuées avec l’instruction raw_input()

print("="*10, "EXO", "="*10,)

name = input('What is yourname : ')

age = input("How old are you : ?")



print("="*10, "CORRECTION", "="*10,)

# programme principal -----------------------------------------------
## instruction input :
nom = input("ton nom ? ")
age = input("age ? ")
age = float(age)
print("\t Nom :", nom, "\t Age :", age)
## bonnes pratiques :
nom = input("ton nom ? ") # pour une chaine
age = float(input("age ? ")) # sinon : transtyper explicitement
print(f'{"-" * 40}\n\t Nom : {nom}\t Age : {age}')


print("="*10, "COMPREHENSION", "="*10,)

print("La bonne pratique est de transtyper en même temps les données lors de la saisie")

