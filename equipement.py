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

    def arme_active(self):
        return self.arme

    def armure_active(self):
        return self.armure


class Objet:
    def __init__(self, nom):
        self.nom = nom


class Arme(Objet):
    def __init__(self, nom, bonus_atk=0, bonus_int=0):
        super().__init__(nom)
        self.bonus_atk = bonus_atk
        self.bonus_int = bonus_int


class Armure(Objet):
    def __init__(self, nom, bonus_def=0, bonus_int=0):
        super().__init__(nom)
        self.bonus_def = bonus_def
        self.bonus_int = bonus_int