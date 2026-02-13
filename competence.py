class Competence:
    def __init__(self, nom):
        self.nom = nom

    def lancer(self, lanceur, cible):
        pass


class CoupPuissant(Competence):
    def __init__(self):
        super().__init__("Coup puissant")

    def lancer(self, lanceur, cible):
        degats = int(lanceur.force * 1.8)
        cible.subir_degats(degats)
        print(f"{lanceur.nom} frappe violemment et inflige {degats} dégâts !")


class ChargeHeroique(Competence):
    def __init__(self):
        super().__init__("Charge héroïque")

    def lancer(self, lanceur, cible):
        degats = int(lanceur.force * 1.2)
        cible.subir_degats(degats)
        print(f"{lanceur.nom} charge et étourdit {cible.nom} !")


class SortBouleDeFeu(Competence):
    def __init__(self):
        super().__init__("Boule de feu")

    def lancer(self, lanceur, cible):
        degats = lanceur.intelligence * 1.5
        cible.subir_degats(degats)
        print(f"{lanceur.nom} lance Boule de feu et inflige {degats} dégâts !")


class SortBouclierArcanique(Competence):
    def __init__(self):
        super().__init__("Bouclier arcanique")

    def lancer(self, lanceur, cible):
        cible.defense += 10
        print(f"{cible.nom} augmente sa défense temporairement !")

class AttaqueSournoise(Competence):
    def __init__(self):
        super().__init__("Attaque sournoise")

    def lancer(self, lanceur, cible):
        degats = int(lanceur.agilite * 1.5)
        cible.subir_degats(degats)
        print(f"{lanceur.nom} frappe dans l’ombre et inflige {degats} dégâts !")


class EsquiveParfaite(Competence):
    def __init__(self):
        super().__init__("Esquive parfaite")

    def lancer(self, lanceur, cible):
        lanceur.agilite * 3
        print(f"{lanceur.nom} se prépare à esquiver la prochaine attaque !")