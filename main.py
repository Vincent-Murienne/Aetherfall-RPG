from personnage import Guerrier, Mage, Voleur
from lieu import Village, Foret, DonjonSalleFinale
from combat import Attaque, Defense, Fuire, UtiliserCompetence
from sauvegarde import menu_sauvegarde, menu_chargement

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
    print("Bienvenue dans le monde Aetherfall")
    print("Votre mission sera de battre le gardien du donjon\n")

def combat(joueur, ennemi):
    print(f"\nCombat : {joueur.nom} VS {ennemi.nom}")

    while joueur.en_vie() and ennemi.en_vie():
        print("\n--- Votre tour ---")
        print("1 - Attaquer")
        print("2 - Compétence")
        print("3 - Défendre")
        print("4 - Fuir")

        choix = input("> ")

        if choix == "1":
            Attaque(joueur, ennemi).executer()
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
            Attaque(ennemi, joueur).executer()

    if joueur.en_vie():
        print("\nVictoire !")
    else:
        print("\nDéfaite...")

def menu_principal(joueur, zone_actuelle, etat_quete, or_possede, ennemis_vaincus, coffres_ouverts):
    while True:
        print("\nMENU PRINCIPAL")
        print("1 - Explorer la zone actuelle")
        print("2 - Se déplacer")
        print("3 - Sauvegarder la partie")
        print("4 - Quitter le jeu")
        
        choix = input("> ").strip()
        
        if choix == "1":
            print(f"\nVous explorez : {zone_actuelle.__class__.__name__}")
            if isinstance(zone_actuelle, (Foret, DonjonSalleFinale)):
                zone_actuelle.direction(combat)
            else:
                zone_actuelle.direction()

        elif choix == "2":
            zone_actuelle = zone_actuelle.se_deplacer()
            if isinstance(zone_actuelle, (Foret, DonjonSalleFinale)):
                zone_actuelle.direction(combat)
            else:
                zone_actuelle.direction()

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
            quitter_jeu(joueur, zone_actuelle, etat_quete, or_possede, ennemis_vaincus, coffres_ouverts)
            break
        else:
            print("\nChoix invalide, veuillez réessayer.")

def quitter_jeu(joueur, zone_actuelle, etat_quete, or_possede, ennemis_vaincus, coffres_ouverts):
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
    elif sous_choix == "2":
        print("\nÀ bientôt !")
    else:
        print("\nRetour au menu principal.")


def jeu():
    intro()
    etat_jeu = menu_chargement()
    
    if etat_jeu:
        joueur = etat_jeu["joueur"]
        zone_actuelle = etat_jeu["zone_actuelle"]
        etat_quete = etat_jeu["etat_quete"]
        or_possede = etat_jeu["or_possede"]
        ennemis_vaincus = etat_jeu["ennemis_vaincus"]
        coffres_ouverts = etat_jeu["coffres_ouverts"]
        print(f"\nBon retour, {joueur.nom} !")
    else:
        joueur = choisir_classe()
        zone_actuelle = Village(joueur)
        etat_quete = 0
        or_possede = 0
        ennemis_vaincus = []
        coffres_ouverts = []
        print("Votre aventure commence au village...\n")
    
    menu_principal(joueur, zone_actuelle, etat_quete, or_possede, ennemis_vaincus, coffres_ouverts)

if __name__ == "__main__":
    jeu()
