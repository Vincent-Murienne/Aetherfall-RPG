import random
from personnage import LoupSauvage, Bandit, Squelette, GardienDonjon

class Village:
    def __init__(self, joueur, magasin):
        self.joueur = joueur
        self.magasin = magasin

    def quitterVillage(self):
        print("Vous quittez le village en direction de la forêt.")
        return Foret(self, self.joueur)


class Foret:
    def __init__(self, village, joueur):
        self.village = village
        self.joueur = joueur
        self.ennemis_standards = [LoupSauvage, Bandit, Squelette]

    def rentrerVillage(self):
        print("Vous retournez au village.")
        return self.village

    def explorerForet(self):
        evenement = random.choice(["combat", "tresor", "rien"])

        if evenement == "combat":
            ennemi = random.choice(self.ennemis_standards)()
            print(f"Un {ennemi.nom} apparaît !")
            return ennemi

        elif evenement == "tresor":
            self.tresor()

        else:
            print("La forêt est calme...")

    def tresor(self):
        print("Vous trouvez un coffre dans les buissons !")

    def rentrerDonjon(self):
        print("Vous trouvez l'entrée du donjon...")
        return DonjonSalle1(self.joueur)


class DonjonSalle1:
    def __init__(self, joueur):
        self.joueur = joueur

    def avancer(self):
        print("Salle 1 terminée.")
        return DonjonSalle2(self.joueur)


class DonjonSalle2:
    def __init__(self, joueur):
        self.joueur = joueur

    def avancer(self):
        print("Salle 2 terminée.")
        return DonjonSalleFinale(self.joueur)


class DonjonSalleFinale:
    def __init__(self, joueur):
        self.joueur = joueur
        self.boss = GardienDonjon()

    def lancerBoss(self):
        print("Le Gardien du Donjon apparaît !")
        return self.boss