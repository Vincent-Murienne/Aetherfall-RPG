class Objet:
    def __init__(self, nom, taille, bonus_atk, bonus_def):
        self.nom = nom
        self.taille = taille
        self.bonus_atk = bonus_atk
        self.bonus_def = bonus_def
    
    def buff_stats(self):
        pass

class Arme(Objet):
    def __init__(self, nom, taille, bonus_atk=0):
        super().__init__(nom, taille, bonus_atk)

    def buff_stats(self):
        pass

class Armure(Objet):
    def __init__(self, nom, taille, bonus_def=0):
        super().__init__(nom, taille, bonus_def)

    def buff_stats(self):
        pass

class Consommable(Objet):
    def __init__(self, nom, taille, bonus_def=0, bonus_atk=0):
        super().__init__(nom, taille, bonus_atk, bonus_def)
    
    def buff_stats(self):
        pass