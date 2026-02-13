from objet import Arme, Armure
class Equipement:
    def __init__(self, porteur):
        self.porteur = porteur
        self.arme = None
        self.armure = None

    def equiper_arme(self, arme):
        self.arme = arme
        print(f"{self.porteur.nom} équipe {arme.nom}")

    def equiper_armure(self, armure):
        self.armure = armure
        print(f"{self.porteur.nom} équipe {armure.nom}")

    def desequiper_arme(self):
        if self.arme:
            print(f"{self.porteur.nom} retire {self.arme.nom}")
            self.arme = None

    def desequiper_armure(self):
        if self.armure:
            print(f"{self.porteur.nom} retire {self.armure.nom}")
            self.armure = None