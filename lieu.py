import random
from personnage import LoupSauvage, Bandit, Squelette, GardienDonjon

class Village:
    def __init__(self, joueur, magasin=None):
        self.joueur = joueur
        self.magasin = magasin
        self.id_zone = "village"

    def direction(self):
        print("Le marchand Jason est présent au village.")
        print("Voulez-vous voir ce qu'il propose ?")
        print("Veuillez saisir : 'Oui' ou 'Non'")
        input("> ").strip()

    def se_deplacer(self):
        print("Vous quittez le village en direction de la forêt.")
        return Foret(self, self.joueur)

class Foret:
    def __init__(self, village, joueur):
        self.village = village
        self.joueur = joueur
        self.ennemis_standards = [LoupSauvage, Bandit, Squelette]
        self.id_zone = "foret"

    def direction(self, combat_func):
        while True:
            print("\nOù voulez-vous aller ?")
            print("1 - Gauche")
            print("2 - Devant")
            print("3 - Droite")
            print("4 - Retour")

            choix = input("> ").strip()

            if choix in ["1", "2", "3"]:
                evenement = random.choice(["combat", "tresor", "rien"])

                if evenement == "combat":
                    ennemi = random.choice(self.ennemis_standards)()
                    print(f"\nUn {ennemi.nom} apparaît !")
                    combat_func(self.joueur, ennemi)

                elif evenement == "tresor":
                    print("\nVous trouvez un coffre !")
                    tresor_cle = random.randint(1, 4)
                    if tresor_cle == 1:
                        if "cle_donjon" not in self.joueur.inventaire:
                            self.joueur.inventaire.append("cle_donjon")
                            print("Vous avez trouvé la CLÉ du Donjon !")
                        else:
                            print("C'est une clé... mais vous l'avez déjà.")
                    else:
                        print("Le trésor ne contient rien.")
                else:
                    print("\nIl n’y a rien ici...")

            elif choix == "4":
                break

    def se_deplacer(self):
        print("1 - Retour au village")
        print("2 - Avancer vers le donjon")
        choix = input("> ").strip()

        if choix == "1":
            return self.village
        elif choix == "2":
            return DonjonSalle1(self.joueur)
        else:
            print("Choix invalide, vous restez dans la forêt.")
            return self

class DonjonSalle1:
    def __init__(self, joueur):
        self.joueur = joueur
        self.id_zone = "donjon_salle1"

    def direction(self):
        print("Vous êtes dans la salle 1 du donjon. Rien à signaler pour le moment.")

    def se_deplacer(self):
        print("Vous avancez vers la salle 2 du donjon...")
        return DonjonSalle2(self.joueur)

class DonjonSalle2:
    def __init__(self, joueur):
        self.joueur = joueur
        self.id_zone = "donjon_salle2"

    def direction(self):
        print("Vous êtes dans la salle 2 du donjon. Rien à signaler pour le moment.")

    def se_deplacer(self):
        print("Vous avancez vers la salle finale du donjon...")
        return DonjonSalleFinale(self.joueur)

class DonjonSalleFinale:
    def __init__(self, joueur):
        self.joueur = joueur
        self.boss = GardienDonjon()
        self.id_zone = "donjon_salle_finale"

    def direction(self, combat_func):
        print(f"\nUn {self.boss.nom} apparaît !")
        combat_func(self.joueur, self.boss)
        if not self.boss.en_vie():
            print("Bien joué champion, tu as vaincu le boss !")

    def se_deplacer(self):
        print("C'est la dernière salle, vous ne pouvez plus avancer.")
        return self
