class Domino:
    def __init__(self, pa, pb):
        self.pa, self.pb = pa, pb

    def affiche_points(self):
        print("Face A :", self.pa, end=' ')
        print("Face B :", self.pb)

    def valeur(self):
        return self.pa + self.pb


d1 = Domino(2, 6)
d2 = Domino(4, 3)
d1.affiche_points()
d2.affiche_points()
print("Total des points : ", d1.valeur() + d2.valeur())
liste_dominos = []

for i in range(7):
    liste_dominos.append(Domino(6, i))
vt = 0
for i in range(7):
    liste_dominos[i].affiche_points()
    vt += liste_dominos[i].valeur()
print("Valeur totale des points : ", vt)
