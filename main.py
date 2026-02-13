from personnage import Guerrier, Mage, Voleur, LoupSauvage, Bandit, Squelette, ChampionCorrompu, GardienDonjon
import random
from lieu import Village
from combat import Attaque, Defense, Fuire, UtiliserCompetence
from sauvegarde import SystemeSauvegarde, menu_sauvegarde, menu_chargement

# Permet au joueur de choisir sa classe
def choisir_classe():
    print("Choisissez votre classe :")
    print("1 - Guerrier")
    print("2 - Mage")
    print("3 - Voleur")
    
    choix = input("> ").strip()
    
    if choix == "1":
        print("\nVous avez choisi le Guerrier !")
        return Guerrier()
    elif choix == "2":
        print("\nVous avez choisi le Mage !")
        return Mage()
    elif choix == "3":
        print("\nVous avez choisi le Voleur !")
        return Voleur()
    else:
        print("Choix invalide, Guerrier sélectionné par défaut.")
        return Guerrier()
    
def intro():
    print("Bienvenu dans le monde Aetherfall")
    print("Votre mission sera de battre le gardien du donjon\n")

def menu_principal(joueur, zone_actuelle, etat_quete, or_possede,ennemis_vaincus, coffres_ouverts):
    while True:
        print("MENU PRINCIPAL")
        print("1 - Explorer la zone actuelle")
        print("2 - Se déplacer")
        print("3 - Sauvegarder la partie")
        print("4 - Quitter le jeu")
        
        choix = input("> ").strip()
            
        if choix == "1":
            print(f"\nVous explorez : {zone_actuelle}")
            direction(joueur, zone_actuelle)

        elif choix == "2":
            zone_actuelle = menu_deplacement(zone_actuelle, joueur)
            direction(joueur, zone_actuelle)
            
        elif choix == "3":
            menu_sauvegarde(
                joueur=joueur,
                zone_actuelle=zone_actuelle,
                etat_quete=etat_quete,
                or_possede=or_possede,
                ennemis_vaincus=ennemis_vaincus,
                coffres_ouverts=coffres_ouverts
            )
            
        elif choix == "4":
            print("QUITTER LE JEU")
            print("Voulez-vous sauvegarder avant de quitter ?")
            print("1 - Oui, sauvegarder et quitter")
            print("2 - Non, quitter sans sauvegarder")
            print("3 - Annuler")
            
            sous_choix = input("> ").strip()
            
            if sous_choix == "1":
                menu_sauvegarde(
                    joueur=joueur,
                    zone_actuelle=zone_actuelle,
                    etat_quete=etat_quete,
                    or_possede=or_possede,
                    ennemis_vaincus=ennemis_vaincus,
                    coffres_ouverts=coffres_ouverts
                )
                print("\nÀ bientôt !")
                break
            elif sous_choix == "2":
                print("\nÀ bientôt !")
                break
            else:
                print("\nRetour au menu principal.")
                
        else:
            print("\nChoix invalide, veuillez réessayer.")

def direction(joueur, zone_actuelle):
    if zone_actuelle == "foret":
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
                        ennemi = random.choice([LoupSauvage, Bandit, Squelette])()
                        print(f"\n Un {ennemi.nom} apparaît !")
                        combat(joueur, ennemi)

                elif evenement == "tresor":
                    print("\n Vous trouvez un coffre !")
                    tresor_cle = random.randint(1,4)
                    if tresor_cle == 1:
                        if "cle_donjon" not in joueur.inventaire:
                            joueur.inventaire.append("cle_donjon")
                            print("Vous avez trouvé la CLÉ du Donjon !")
                        else:
                            print("C'est une clé... mais vous l'avez déjà.")
                    else:
                        print("Le trésor ne contient rien.")
                else:
                    print("\n Il n’y a rien ici...")

            elif choix == "4":
                break

    elif zone_actuelle == "village":
        print("Le marchand Jason est présent au village")
        print("Voulez-vous voir ce qu'il propose ?")
        print("Veuillez saisir : 'Oui' ou 'Non'")
        reponse = input("> ").strip()

    elif zone_actuelle == "donjon":
        ennemi = ChampionCorrompu()
        print(f"\n Un {ennemi.nom} apparaît !")
        combat(joueur, ennemi)

        if ennemi.en_vie == False:
            print("Bien joué champion, tu as vaincu le boss")

def menu_deplacement(zone_actuelle, joueur):
    print("SE DÉPLACER")
    print("1 - Village")
    print("2 - Forêt")
    print("3 - Donjon")
    print("4 - Rester ici")

    choix = input("> ").strip()

    if choix == "1":
        return "village"
    elif choix == "2":
        return "foret"
    elif choix == "3":
        if "cle_donjon" in joueur.inventaire: 
            print("La clé ouvre la porte du donjon...")           
            return "donjon"
        else:
            print("Vous n'avez pas la clé du Donjon")
            return
    else:
        return zone_actuelle

# Fonction principale du jeu avec gestion de la sauvegarde
def jeu():
    intro()
    etat_jeu = menu_chargement()
    
    if etat_jeu:
        # Partie chargée
        joueur = etat_jeu["joueur"]
        zone_actuelle = etat_jeu["zone_actuelle"]
        etat_quete = etat_jeu["etat_quete"]
        or_possede = etat_jeu["or_possede"]
        ennemis_vaincus = etat_jeu["ennemis_vaincus"]
        coffres_ouverts = etat_jeu["coffres_ouverts"]
        
        print(f"\nBon retour, {joueur.nom} !")
    else:
        # Nouvelle partie
        joueur = choisir_classe()
        zone_actuelle = "village"
        etat_quete = 0
        or_possede = 0
        ennemis_vaincus = []
        coffres_ouverts = []
        
        print("Votre aventure commence au village...\n")
    
    menu_principal(
        joueur=joueur,
        zone_actuelle=zone_actuelle,
        etat_quete=etat_quete,
        or_possede=or_possede,
        ennemis_vaincus=ennemis_vaincus,
        coffres_ouverts=coffres_ouverts
    )

def combat(joueur, ennemi):
    print(f"\n Combat : {joueur.nom} VS {ennemi.nom} ")

    while joueur.en_vie() and ennemi.en_vie():

        print("\n--- Votre tour ---")
        print("1 - Attaquer")
        print("2 - Compétence")
        print("3 - Défendre")
        print("4 - Fuir")

        choix = input("> ")

        if choix == "1":
            action = Attaque(joueur, ennemi)
            action.executer()

        elif choix == "2":
            for i, c in enumerate(joueur.competences):
                print(f"{i+1} - {c.nom}")
            index = int(input("> ")) - 1
            UtiliserCompetence(joueur, joueur.competences[index], ennemi).executer()

        elif choix == "3":
            Defense(joueur).executer()

        elif choix == "4":
            if Fuire(joueur).executer():
                return
        else:
            print("Choix invalide.")
            continue

        if ennemi.en_vie():
            print("\n--- Tour ennemi ---")
            action = Attaque(ennemi, joueur)
            action.executer()

    if joueur.en_vie():
        print("\n Victoire !")
    else:
        print("\n Défaite...")

if __name__ == "__main__":
    jeu()