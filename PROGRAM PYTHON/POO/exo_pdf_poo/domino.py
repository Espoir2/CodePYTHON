# Créer une classe Domino (fichier CDomino.py) qui se définit par la valeur des points sur ce dernier.
# La classe CDomino aura 2 méthodes :
# — affiche_points qui affiche le domino
# — valeur qui donne la somme des points du domino
# Écrire un programme domino.py qui instancie cette classe et utilise ses méthodes :
# — Créer 2 dominos [2,6] et [4,3] et leur appliquer les méthodes
# — Créer une liste de 7 dominos [6,valeur de 1 à 6] qui les affiche puis indique la somme de l’ensemble


def afficher_list(the_list):
    for i in the_list:
        print(i, end=" ")


class Domino:
    def __init__(self, name, pa, pb):
        self.name = name
        print(self.name)
        self.pa = pa
        self.pb = pb

    def __str__(self):
        return self.name

    def affiche_points(self):
        pa = []
        pb = []
        for _ in range(self.pa):
            pa.append("⚪")
        for _ in range(self.pb):
            pb.append("🟣")
        print("pa : ", end="")
        afficher_list(pa)
        print()

        print("pb : ", end="")
        afficher_list(pb)
        print()

    def valeur(self):
        print(f"total_points = {self.pa + self.pb}")


domino_01 = Domino("domino_01", 3, 4)
domino_01.affiche_points()
domino_01.valeur()

print("-" * 100)

domino_02 = Domino("domino_02", 5, 4)
domino_02.affiche_points()
domino_02.valeur()

# domino1 = Domino(6, 1)
# domino2 = Domino(6, 2)
# domino1 = Domino(6, 3)
# domino1 = Domino(6, 4)
# domino1 = Domino(6, 5)
# domino1 = Domino(6, 6)

print("=" * 100)

list_dominos = [Domino("domino(6,1)", 6, 1), Domino("domino(6,2)", 6, 2),
                Domino("domino(6,3)", 6, 3), Domino("domino(6,4)", 6, 4),
                Domino("domino(6,5)", 6, 5), Domino("domino(6,6)", 6, 6)]
total_points = 0
for domino in list_dominos:
    print(domino)
    domino.affiche_points()
    total_points += domino.pa + domino.pb
    print("-" * 100)
print(f"Le nombre total de points de la liste de 6 dominos est : {total_points}")

# SEE THE ANSWER FOR CODE IMPROVEMENT
