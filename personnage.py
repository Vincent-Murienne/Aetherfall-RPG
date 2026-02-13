import random
from equipement import Equipement
from competence import CoupPuissant, ChargeHeroique, SortBouleDeFeu, SortBouclierArcanique, AttaqueSournoise, EsquiveParfaite

class Personnage:
    def __init__(self, nom, max_pv, force, intelligence, agilite, defense, inventaire, argent, taux_critique):
        self.nom = nom
        self.max_pv = max_pv
        self.pv_actuels = max_pv
        self.force = force
        self.intelligence = intelligence
        self.agilite = agilite
        self.defense = defense
        self.taux_critique = taux_critique
        self.equipement = Equipement(self)
        self.statuts = []
        self.inventaire = inventaire
        self.argent = argent

    @property
    def force_totale(self):
        bonus = 0
        if self.equipement.arme:
            bonus += self.equipement.arme.bonus_atk
        return self.force + bonus

    @property
    def defense_totale(self):
        bonus = 0
        if self.equipement.armure:
            bonus += self.equipement.armure.bonus_def
        return self.defense + bonus

    def en_vie(self):
        return self.pv_actuels > 0

    def subir_degats(self, montant):
        degats_reels = max(0, montant - (self.defense_totale))
        self.pv_actuels -= degats_reels
        self.pv_actuels = max(0, self.pv_actuels)

    def soigner(self, montant):
        self.pv_actuels = min(self.max_pv, self.pv_actuels + montant)

    def ajouter_statut(self, effet):
        self.statuts.append(effet)

    def AfficherBourse(self):
        print(self.argent)

    def bourse(self, argent_gagne):
        self.argent += argent_gagne
        return self.argent

    def afficherInventaire(self):
        if(len(self.inventaire) > 0):
            index = 0
            for i in self.inventaire:
                print(index,": ", i)
                index += 1
        else:
            print("inventaire vide")
            return

    def SupprimerInventaire(self, index):
        self.inventaire.pop(index)

    def loot(self, cible):
        if(cible.pv_actuels <= 0):

            self.bourse(cible.argent)
            if(len(self.inventaire) < 10):
                self.inventaire.extend(cible.inventaire)
                cible.inventaire = []
            else:
                print("Vous pouvez pas porter plus d'objet")
        
        return self.inventaire

    # def appliquer_effets(self, moment):
    #     for effet in self.statuts[:]:
    #         if effet.moment == moment and effet.actif:
    #             effet.appliquer(self)

    #             if effet.duree <= 0:
    #                 effet.expirer(self)
    #                 self.statuts.remove(effet)

    def choisir_action(self):
        print("L'ennemi et nous, choisissons une action")


class PersonnageJouable(Personnage):
    def __init__(self, nom, max_pv, force, intelligence, agilite, defense, inventaire, argent, taux_critique=0.05):
        super().__init__(nom, max_pv, force, intelligence, agilite, defense, inventaire, argent, taux_critique)

        self.competences = []

    def ajouter_competence(self, competence):
        self.competences.append(competence)

    def choisir_action(self):
        return self.competences

class Guerrier(PersonnageJouable):
    def __init__(self):
        super().__init__(
            nom="Guerrier",
            max_pv=120,
            force=70,
            intelligence=20,
            agilite=30,
            defense=60,
            taux_critique=0.05,
            inventaire=[],
            argent=20
        )

        self.ajouter_competence(CoupPuissant())
        self.ajouter_competence(ChargeHeroique())

class Mage(PersonnageJouable):
    def __init__(self):
        super().__init__(
            nom="Mage",
            max_pv=80,
            force=20,
            intelligence=80,
            agilite=40,
            defense=30,
            taux_critique=0.05,
            inventaire=[],
            argent=5
        )

        self.ajouter_competence(SortBouleDeFeu())
        self.ajouter_competence(SortBouclierArcanique())

class Voleur(PersonnageJouable):
    def __init__(self):
        super().__init__(
            nom="Voleur",
            max_pv=90,
            force=35,
            intelligence=30,
            agilite=80,
            defense=40,
            taux_critique=0.15,
            inventaire=[],
            argent=35
        )

        self.ajouter_competence(AttaqueSournoise())
        self.ajouter_competence(EsquiveParfaite())


class Bestiaire(Personnage):
    def __init__(self, nom, max_pv, force, intelligence, agilite, defense, inventaire, argent, taux_critique=0.05):
        super().__init__(nom, max_pv, force, intelligence, agilite, defense, inventaire, argent, taux_critique)

        self.competences = []

    def ajouter_competence(self, competence):
        self.competences.append(competence)

    def choisir_action(self):
        # Pour l’instant : attaque aléatoire simple
        if self.competences:
            return random.choice(self.competences)


# rajouter -> attaques multiples, vol d'objets possible, résistant aux dégâts physiques
class LoupSauvage(Bestiaire):
    def __init__(self):
        super().__init__(
            nom="Loup sauvage",
            max_pv=60,
            force=35,
            intelligence=10,
            agilite=70,
            defense=20,
            taux_critique=0.1,
            inventaire=["viande", "os"],
            argent=3
        )

    def attaqueRapide(self, cible):
        pass


# rajouter -> vol d'objets possible, résistant aux dégâts physiques
class Bandit(Bestiaire):
    def __init__(self):
        super().__init__(
            nom="Bandit",
            max_pv=80,
            force=40,
            intelligence=20,
            agilite=50,
            defense=30,
            taux_critique=0.12,
            invenaire=["tissus"],
            argent=5
        )
        
    def vole_argent(self, cible):
        cible.argent -= 10

# rajouter -> résistant aux dégâts physiques
class Squelette(Bestiaire):
    def __init__(self):
        super().__init__(
            nom="Squelette",
            max_pv=90,
            force=45,
            intelligence=5,
            agilite=30,
            defense=60,   # grosse défense physique
            taux_critique=0.05,
            inventaire=["os"],
            argent=7
        )

    def resistancePhysique(self, cible):
        pass

# rajouter -> PV élevés et compétence spéciale
class ChampionCorrompu(Bestiaire):
    def __init__(self):
        super().__init__(
            nom="Champion corrompu",
            max_pv=200,
            force=60,
            intelligence=15,
            agilite=30,
            defense=60,
            taux_critique=0.05,
            inventaire=[],
            argent=20
        )

    def coupUltraPuissant(self, cible):
        pass

class GardienDonjon(Bestiaire):
    def __init__(self):
        super().__init__(
            nom="Gardien du donjon",
            max_pv=250,
            force=70,
            intelligence=50,
            agilite=40,
            defense=70,
            taux_critique=0.15,
            inventaire=[],
            argent=100
        )

        self.phase = 1

        self.ajouter_competence(CoupPuissant())
        self.ajouter_competence(SortBouleDeFeu())

    def maxiBuff(self, cible):
        pass

    def subir_degats(self, montant):
        super().subir_degats(montant)

        if self.phase == 1 and self.pv_actuels <= self.max_pv * 0.5:
            self.passer_phase_2()

    def passer_phase_2(self):
        self.phase = 2
        self.force += 20
        self.agilite += 20
        print("Le Gardien entre en phase 2 ! Il devient furieux !")


