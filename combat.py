import random

class Combat:
    def __init__(self, lanceur, cible=None):
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        raise NotImplementedError("Chaque action de combat doit implémenter executer()")

class Attaque(Combat):
    def __init__(self, lanceur, cible, effet=None):
        super().__init__(lanceur, cible)
        self.effet = effet

    def executer(self):
        attaque = self.lanceur.force_totale

        if random.randint(1,100) <= self.lanceur.taux_critique * 100:
            degats = int(attaque * 1.5)
            print("Coup critique !")
        else:
            degats = attaque

        self.cible.subir_degats(degats)
        print(f"{self.lanceur.nom} attaque {self.cible.nom}.")

        # Ajout d’effet (poison, étourdissement, etc.)
        # if self.effet:
        #     self.cible.ajouter_statut(self.effet)
        #     print(f"{self.cible.nom} est affecté par {self.effet.nom} !")

class Defense(Combat):
    def executer(self):
        self.lanceur.defense += 15
        print(f"{self.lanceur.nom} se met en position défensive.")

class Consommer(Combat):
    def __init__(self, lanceur, objet):
        super().__init__(lanceur)
        self.objet = objet

    def executer(self):
        self.objet.utiliser(self.lanceur)
        print(f"{self.lanceur.nom} utilise {self.objet.nom}.")

class UtiliserCompetence(Combat):
    def __init__(self, lanceur, competence, cible):
        super().__init__(lanceur, cible)
        self.competence = competence

    def executer(self):
        self.competence.lancer(self.lanceur, self.cible)

class Fuire(Combat):
    def executer(self):
        chance = 0.4 + self.lanceur.agilite / 200

        if random.random() < chance:
            print(f"{self.lanceur.nom} réussit à fuir le combat !")
            return True
        else:
            print(f"{self.lanceur.nom} échoue à fuir...")
            return False