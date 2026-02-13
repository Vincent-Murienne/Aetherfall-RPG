from combat import Attaque, Defense

class AttaqueEffet(Attaque):
    def __init__(self, nom, duree, moment):
        self.nom = nom
        self.duree = duree
        self.moment = moment  # "debut_tour", "impact", "fin_tour"
        self.actif = True

    def appliquer(self, cible):
        pass

    def expirer(self, cible):
        self.actif = False
        print(f"{self.nom} sur {cible.nom} a expiré.")

class Poison(AttaqueEffet):
    def __init__(self, degats=5, duree=3):
        super().__init__("Poison", duree, moment="debut_tour")
        self.degats = degats

    def appliquer(self, cible):
        print(f"{cible.nom} subit {self.degats} dégâts de poison.")
        cible.subir_degats(self.degats)
        self.duree -= 1

    def expirer(self, cible):
        self.actif = False
        print(f"{self.nom} sur {cible.nom} a expiré.")

class Etourdissement(AttaqueEffet):
    def __init__(self):
        super().__init__("Étourdissement", 1, moment="debut_tour")

    def appliquer(self, cible):
        cible.est_etourdi = True
        print(f"{cible.nom} est étourdi et saute son tour.")
        self.duree -= 1

    def expirer(self, cible):
        self.actif = False
        print(f"{self.nom} sur {cible.nom} a expiré.")

class DefenseEffet(Defense):
    def __init__(self, nom, duree, moment):
        self.nom = nom
        self.duree = duree
        self.moment = moment  # "debut_tour", "impact", "fin_tour"
        self.actif = True

    def appliquer(self, cible):
        pass

    def expirer(self, cible):
        pass

class Bouclier(DefenseEffet):
    def __init__(self, valeur=20, duree=3):
        super().__init__("Bouclier", duree, moment="impact")
        self.valeur = valeur

    def appliquer(self, cible, degats):
        return degats
    
    def expirer(self, cible):
        self.actif = False
        print(f"{self.nom} sur {cible.nom} a expiré.")