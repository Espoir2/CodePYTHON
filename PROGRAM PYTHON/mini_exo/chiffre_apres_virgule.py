# Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
# Calculez et affichez la valeur de la vitesse.
# Améliorez l’affichage en imposant un chiffre après le point décimal.


print("="*10, "EXO", "="*10,)

temps = 6.892
distance = 19.7

vitesse = distance / temps

print(f"Vitesse = {vitesse}")




# ❓ Recherche : 
# Comment afficher un float avec un nombrte précis de chiffre après la virgule

print("="*10, "CORRECTION", "="*10,)


# Correction : 
# programme principal -----------------------------------------------
## affichage simple :
temps = 6.892
distance = 19.7
vitesse = distance/temps
print("vitesse =", vitesse)
## affichage formate :
print(f'{"-" * 23}')
print("\n vitesse = {:.2f} m/s".format(vitesse)) # arrondi a 2 chiffres


print("="*10, "COMPREHENSION", "="*10,)

nbr = 10 / 3

print(f"10/3 = {nbr:.2f} ")