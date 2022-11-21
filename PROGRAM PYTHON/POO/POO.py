# Les classes

from pprint import pprint


class Ordinateur:
    marque = "hp"
    couleur = "Argent"


print(Ordinateur.marque)
print("-" * 100)


class Portable:
    nbr = 0

    def __init__(self, marque) -> None:
        self.marque = marque
        Portable.nbr += 1

    def afficher_marque(self):
        print(f"La marque de ce portable est {self.marque}")


mon_portable = Portable("TECNO")

print(mon_portable)
print(Portable.nbr)
mon_portable.afficher_marque()

print("-" * 100)


# Encapsulation
# 01 Les Attributs privés __attributs

class Animal:

    def __init__(self, race) -> None:
        self.__race = race

    def get_race(self):
        return self.__race

    def set_race(self, nouvelleRace):
        self.__race = nouvelleRace
        return


lion_01 = Animal("LION")
print(lion_01.get_race())
lion_01.__race = "lion de la savane"
print(lion_01.get_race())
lion_01.set_race("Lion de la savane")
print(lion_01.get_race())

print("-" * 100)


# Heritage
class App_technologiques:
    nbr_AT = 0

    def __init__(self, marque="sans marque", couleur="sans couleur") -> None:
        self.marque = marque
        self.couleur = couleur
        self.nbr_AT += 1

    @classmethod  # Intègre la fonction dans toutes les instance de la class
    def nbr_crees(cls):
        cls.nbr_AT += 1
        return cls.nbr_AT

    @staticmethod
    def total(a, b):
        return a + b


class Pc(App_technologiques):
    def __init__(self, ram_gb, nbr_processeur, marque="sans marque", couleur="sans couleur") -> None:
        super().__init__(marque, couleur)
        self.ram_gb = ram_gb
        self.processeur = nbr_processeur
        self.nbr_crees()


class Phone(App_technologiques):
    def __init__(self, camera, marque="sans marque", couleur="sans couleur") -> None:
        super().__init__(marque, couleur)
        self.camera = camera
        self.nbr_crees()


my_pc = Pc("16gb", "8 CPUs", "hp", "Argent")

my_pc_02 = Pc("8gb", "4 CPUs", "Asus", "Noir")

my_phone = Phone("800 Megapixels", "Tecno", "Bleue")

print("my_pc : ", my_pc.marque, "/", my_pc.couleur, "/", my_pc.ram_gb, "/", my_pc.processeur)
print("*" * 10)
print("my_pc_02 : ", my_pc_02.marque, "/", my_pc_02.couleur, "/", my_pc_02.ram_gb, "/", my_pc_02.processeur)
print("*" * 10)
print("my_phone : ", my_pc.marque, "/", my_pc.couleur, "/", my_phone.camera)
print("*" * 10)

print(f" Le nombre d'ordinateurs est : {Pc.nbr_AT}")
print(f" Le nombre de portable est :  {Phone.nbr_AT}")
print(f" Le nombre total d'appareils technologiques créés est : {App_technologiques.total(Pc.nbr_AT, Phone.nbr_AT)}")

# ---*FONCTIONS UTILES*---#
# pprint(dir(App_technologiques))
# isinstance(instance, class)
# issubclass(subclass, class)
# instance.__dict__ : Permet de récuppérer tous les attributs d'une instance dans un dictionnaire
