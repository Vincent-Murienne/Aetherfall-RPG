import json
import os
from datetime import datetime
from personnage import Guerrier, Mage, Voleur
from equipement import Arme, Armure
from lieu import Village, Foret, DonjonSalle1, DonjonSalle2, DonjonSalleFinale


# Système de sauvegarde et chargement de partie en JSON.
# Gère la persistance de l'état complet du jeu

class SystemeSauvegarde:
    DOSSIER_SAUVEGARDES = "sauvegardes"
    FICHIER_SAUVEGARDE = "partie.json"
    
    def __init__(self):
        # On crée le dossier de sauvegardes s'il n'existe pas.
        if not os.path.exists(self.DOSSIER_SAUVEGARDES):
            os.makedirs(self.DOSSIER_SAUVEGARDES)
    
    # On sauvegarde l'état complet de la partie en JSON.
    def sauvegarder(self, joueur, zone_actuelle, etat_quete=0, or_possede=0, 
                    ennemis_vaincus=None, coffres_ouverts=None):
        
        if ennemis_vaincus is None:
            ennemis_vaincus = []
        if coffres_ouverts is None:
            coffres_ouverts = []
        
        try:
            # Construction du dictionnaire de données
            donnees = {
                "date_sauvegarde": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                
                # Données du personnage
                "personnage": {
                    "classe": joueur.nom,
                    "pv_actuels": joueur.pv_actuels,
                    "pv_max": joueur.max_pv,
                    "force": joueur.force,
                    "intelligence": joueur.intelligence,
                    "agilite": joueur.agilite,
                    "defense": joueur.defense,
                    "taux_critique": joueur.taux_critique
                },
                
                # Inventaire
                "inventaire": {
                    "objets": self._serialiser_inventaire(joueur),
                    "arme_equipee": self._serialiser_arme(joueur.equipement.arme),
                    "armure_equipee": self._serialiser_armure(joueur.equipement.armure)
                },
                
                # Progression
                "progression": {
                    "zone_actuelle": zone_actuelle,
                    "etat_quete": etat_quete
                },
                
                # Données optionnelles
                "donnees_optionnelles": {
                    "or_possede": or_possede,
                    "ennemis_vaincus": ennemis_vaincus,
                    "coffres_ouverts": coffres_ouverts
                }
            }
            
            # JSON du fichier 
            chemin_complet = os.path.join(self.DOSSIER_SAUVEGARDES, self.FICHIER_SAUVEGARDE)
            with open(chemin_complet, 'w', encoding='utf-8') as fichier:
                json.dump(donnees, fichier, indent=4, ensure_ascii=False)
            
            print(f"\nPartie sauvegardée avec succès dans '{chemin_complet}'")
            return True
            
        except Exception as e:
            print(f"\nErreur lors de la sauvegarde : {e}")
            return False
    
    # On charge la partie sauvegardée depuis le fichier JSON.
    def charger(self):

        chemin_complet = os.path.join(self.DOSSIER_SAUVEGARDES, self.FICHIER_SAUVEGARDE)
        
        if not os.path.exists(chemin_complet):
            print("Aucune sauvegarde trouvée.")
            return None
        
        try:
            # Lecture du fichier JSON
            with open(chemin_complet, 'r', encoding='utf-8') as fichier:
                donnees = json.load(fichier)
            
            # On reconstruction du personnage
            joueur = self._deserialiser_personnage(donnees["personnage"])
            
            # On reconstruction de l'équipement
            if donnees["inventaire"]["arme_equipee"]:
                arme = self._deserialiser_arme(donnees["inventaire"]["arme_equipee"])
                joueur.equipement.equiper_arme(arme)
            
            if donnees["inventaire"]["armure_equipee"]:
                armure = self._deserialiser_armure(donnees["inventaire"]["armure_equipee"])
                joueur.equipement.equiper_armure(armure)
            
            # On préparation de l'état du jeu
            etat_jeu = {
                "joueur": joueur,
                "zone_actuelle": donnees["progression"]["zone_actuelle"],
                "etat_quete": donnees["progression"]["etat_quete"],
                "or_possede": donnees["donnees_optionnelles"]["or_possede"],
                "ennemis_vaincus": donnees["donnees_optionnelles"]["ennemis_vaincus"],
                "coffres_ouverts": donnees["donnees_optionnelles"]["coffres_ouverts"],
                "inventaire_objets": donnees["inventaire"]["objets"]
            }
            
            date_sauvegarde = donnees.get("date_sauvegarde", "inconnue")
            print(f"\n Partie chargée avec succès (sauvegardée le {date_sauvegarde})")
            
            return etat_jeu
            
        except Exception as e:
            print(f"\n Erreur lors du chargement : {e}")
            return None
    
    # On vérifie si une sauvegarde existe.
    def sauvegarde_existe(self):
        chemin_complet = os.path.join(self.DOSSIER_SAUVEGARDES, self.FICHIER_SAUVEGARDE)
        return os.path.exists(chemin_complet)
    
    # On supprime la sauvegarde existante.
    def supprimer_sauvegarde(self):
        chemin_complet = os.path.join(self.DOSSIER_SAUVEGARDES, self.FICHIER_SAUVEGARDE)
        
        if not os.path.exists(chemin_complet):
            print("\n Aucune sauvegarde à supprimer.")
            return False
        
        try:
            os.remove(chemin_complet)
            print("\n Sauvegarde supprimée avec succès.")
            return True
        except Exception as e:
            print(f"\n Erreur lors de la suppression : {e}")
            return False
    

    # ==================== ZONE METHODES DE SÉRIALISATION ====================
    
   
    def _serialiser_inventaire(self, joueur):
        # À compléter en fonction des besoin
        return []
    
    def _serialiser_arme(self, arme):
        # On sérialise une arme en dictionnaire.

        if arme is None:
            return None
        
        return {
            "nom": arme.nom,
            "bonus_atk": arme.bonus_atk,
            "bonus_int": arme.bonus_int
        }
    
    def _serialiser_armure(self, armure):
        # On sérialise une armure en dictionnaire.

        if armure is None:
            return None
        
        return {
            "nom": armure.nom,
            "bonus_def": armure.bonus_def,
            "bonus_int": armure.bonus_int
        }
    
    # ==================== ZONE METHODES DE DÉSÉRIALISATION ====================
    
    # On reconstruit un personnage depuis les données JSON
    def _deserialiser_personnage(self, donnees_perso):
        classe = donnees_perso["classe"]
        
        if classe == "Guerrier":
            joueur = Guerrier()
        elif classe == "Mage":
            joueur = Mage()
        elif classe == "Voleur":
            joueur = Voleur()
        else:
            raise ValueError(f"Classe inconnue : {classe}")
        
        joueur.pv_actuels = donnees_perso["pv_actuels"]
        joueur.max_pv = donnees_perso["pv_max"]
        joueur.force = donnees_perso["force"]
        joueur.intelligence = donnees_perso["intelligence"]
        joueur.agilite = donnees_perso["agilite"]
        joueur.defense = donnees_perso["defense"]
        joueur.taux_critique = donnees_perso["taux_critique"]
        
        return joueur
    
    # On reconstruit une arme depuis les données JSON.
    def _deserialiser_arme(self, donnees_arme):
        if donnees_arme is None:
            return None
        
        return Arme(
            nom=donnees_arme["nom"],
            bonus_atk=donnees_arme["bonus_atk"],
            bonus_int=donnees_arme["bonus_int"]
        )
    
    # On reconstruit une armure depuis les données JSON.
    def _deserialiser_armure(self, donnees_armure):
        if donnees_armure is None:
            return None
        
        return Armure(
            nom=donnees_armure["nom"],
            bonus_def=donnees_armure["bonus_def"],
            bonus_int=donnees_armure["bonus_int"]
        )
    
    # On reconstruit l'objet de zone depuis son nom.
    def _deserialiser_zone(self, nom_zone, joueur):
        if nom_zone == "village":
            return Village(joueur, magasin=None)
        elif nom_zone == "foret":
            village = Village(joueur, magasin=None)
            return Foret(village, joueur)
        elif nom_zone == "donjon_salle1":
            return DonjonSalle1(joueur)
        elif nom_zone == "donjon_salle2":
            return DonjonSalle2(joueur)
        elif nom_zone == "donjon_salle_finale":
            return DonjonSalleFinale(joueur)
        else:
            # Par défaut, retour au village
            return Village(joueur, magasin=None)


# ==================== ZONE FONCTIONS UTILITAIRES ====================

def menu_sauvegarde(joueur, zone_actuelle, etat_quete=0, or_possede=0, 
                    ennemis_vaincus=None, coffres_ouverts=None):
    
    print("MENU DE SAUVEGARDE")
    print("Voulez-vous sauvegarder votre partie ?")
    print("1 - Oui, sauvegarder")
    print("2 - Non, annuler")
    
    choix = input("> ").strip()
    
    if choix == "1":
        systeme = SystemeSauvegarde()
        return systeme.sauvegarder(
            joueur=joueur,
            zone_actuelle=zone_actuelle,
            etat_quete=etat_quete,
            or_possede=or_possede,
            ennemis_vaincus=ennemis_vaincus,
            coffres_ouverts=coffres_ouverts
        )
    else:
        print("\nSauvegarde annulée.")
        return False


# On affiche un menu de chargement et charge une partie si demandé
def menu_chargement():
    systeme = SystemeSauvegarde()
    
    if not systeme.sauvegarde_existe():
        print("\nAucune sauvegarde trouvée. Nouvelle partie...")
        return None
    
    print("MENU DE CHARGEMENT")
    print("Une sauvegarde a été trouvée.")
    print("1 - Charger la partie")
    print("2 - Nouvelle partie")
    
    choix = input("> ").strip()
    
    if choix == "1":
        return systeme.charger()
    else:
        print("\nNouvelle partie lancée...")
        return None
