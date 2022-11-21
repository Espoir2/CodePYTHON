# Créer une classe Cercle (fichier CCercle.py) qui se définit par son rayon.
# La classe CCercle aura 2 méthodes, qui permettront de calculer l’aire (π × r
# 2
# ) et le périmètre (2 ×
# π × r).
# Écrire un programme cercle.py qui instancie cette classe et utilise ses méthodes

from math import *


class Ccercle:
    def __init__(self, r):
        self.ray = r

    def __str__(self):
        return f"The circle of ray : {self.ray}"

    def area(self):
        return self.ray ** 2 * pi

    def perimeter(self):
        return 2 * pi * self.ray


circle_01 = Ccercle(4)
print(circle_01)
print(circle_01.area(), circle_01.perimeter())

print("-" * 100)

circle_02 = Ccercle(5)
print(circle_02)
print(circle_02.area(), circle_02.perimeter())
