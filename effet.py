class Effet:
    def __init__(self, nom, duree, moment="debut_tour"):
        self.nom = nom
        self.duree = duree
        self.moment = moment  # "debut_tour", "impact", "fin_tour"
        self.actif = True

    def appliquer(self, cible):
        pass

    def expirer(self, cible):
        self.actif = False
        print(f"{self.nom} sur {cible.nom} a expiré.")

class AttaqueEffet(Effet):
    def __init__(self, nom, duree, moment="debut_tour"):
        super().__init__(nom, duree, moment)


class Poison(AttaqueEffet):
    def __init__(self, degats=5, duree=3):
        super().__init__("Poison", duree, moment="debut_tour")
        self.degats = degats

    def appliquer(self, cible):
        print(f"{cible.nom} subit {self.degats} dégâts de poison.")
        cible.subir_degats(self.degats)
        self.duree -= 1


class Etourdissement(AttaqueEffet):
    def __init__(self):
        super().__init__("Étourdissement", 1, moment="debut_tour")

    def appliquer(self, cible):
        cible.est_etourdi = True
        print(f"{cible.nom} est étourdi et saute son tour.")
        self.duree -= 1


class DefenseEffet(Effet):
    def __init__(self, nom, duree, moment="impact"):
        super().__init__(nom, duree, moment)


class Bouclier(DefenseEffet):
    def __init__(self, valeur=20, duree=3):
        super().__init__("Bouclier", duree, moment="impact")
        self.valeur = valeur

    def appliquer(self, cible, degats):
        absorb = min(self.valeur, degats)
        self.valeur -= absorb
        degats -= absorb

        print(f"Bouclier absorbe {absorb} dégâts.")

        if self.valeur <= 0:
            self.duree = 0

        return degats