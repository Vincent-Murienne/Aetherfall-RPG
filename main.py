from personnage import Guerrier, Mage, Voleur
from lieu import Village
from sauvegarde import SystemeSauvegarde, menu_sauvegarde, menu_chargement


# Permet au joueur de choisir sa classe
def choisir_classe():
    print("Choisissez votre classe :")
    print("1 - Guerrier (PV: 120, Force: 70, Défense: 60)")
    print("2 - Mage (PV: 80, Intelligence: 80, Agilité: 40)")
    print("3 - Voleur (PV: 90, Agilité: 80, Critique: 15%)")
    
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


# Affiche les statistiques actuelles du joueur
def afficher_statut_joueur(joueur, or_possede=0, etat_quete=0):
    print(f"STATUT - {joueur.nom}")
    print(f"PV: {joueur.pv_actuels}/{joueur.max_pv}")
    print(f"Force: {joueur.force_totale} | Intelligence: {joueur.intelligence}")
    print(f"Agilité: {joueur.agilite} | Défense: {joueur.defense_totale}")
    
    if joueur.equipement.arme:
        print(f"Arme: {joueur.equipement.arme.nom}")
    if joueur.equipement.armure:
        print(f"Armure: {joueur.equipement.armure.nom}")
    
    print(f"Or: {or_possede}")
    
    etats_quete = {0: "Non commencée", 1: "En cours", 2: "Terminée"}
    print(f"Quête principale: {etats_quete.get(etat_quete, 'Inconnue')}")


# Menu principal du jeu avec options de jeu et sauvegarde.
def menu_principal(joueur, zone_actuelle, etat_quete, or_possede,ennemis_vaincus, coffres_ouverts):
    while True:
        print("MENU PRINCIPAL")
        print("1 - Voir mon statut")
        print("2 - Explorer la zone actuelle")
        print("3 - Se déplacer")
        print("4 - Sauvegarder la partie")
        print("5 - Quitter le jeu")
        
        choix = input("> ").strip()
        
        if choix == "1":
            afficher_statut_joueur(joueur, or_possede, etat_quete)
            
        elif choix == "2":
            print(f"\nVous explorez : {zone_actuelle}")
            # Logique d'exploration à implémenter selon la zone
            
        elif choix == "3":
            zone_actuelle = menu_deplacement(zone_actuelle)
            
        elif choix == "4":
            menu_sauvegarde(
                joueur=joueur,
                zone_actuelle=zone_actuelle,
                etat_quete=etat_quete,
                or_possede=or_possede,
                ennemis_vaincus=ennemis_vaincus,
                coffres_ouverts=coffres_ouverts
            )
            
        elif choix == "5":
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
                print("\nÀ bientôt, aventurier !")
                break
            elif sous_choix == "2":
                print("\nÀ bientôt, aventurier !")
                break
            else:
                print("\nRetour au menu principal.")
                
        else:
            print("\nChoix invalide, veuillez réessayer.")


# Menu de déplacement entre les zones.
def menu_deplacement(zone_actuelle):
    print("SE DÉPLACER")
    print("Où voulez-vous aller ?")
    print("1 - Village")
    print("2 - Forêt")
    print("3 - Donjon (salle 1)")
    print("4 - Rester ici")
    
    choix = input("> ").strip()
    
    if choix == "1":
        print("\nVous vous dirigez vers le village...")
        return "village"
    elif choix == "2":
        print("\nVous vous dirigez vers la forêt...")
        return "foret"
    elif choix == "3":
        print("\nVous entrez dans le donjon...")
        return "donjon_salle1"
    else:
        print(f"\nVous restez dans : {zone_actuelle}")
        return zone_actuelle


# Fonction principale du jeu avec gestion de la sauvegarde
def jeu():

    # Tentative de chargement d'une partie existante
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
        afficher_statut_joueur(joueur, or_possede, etat_quete)
    else:
        # Nouvelle partie
        joueur = choisir_classe()
        zone_actuelle = "village"
        etat_quete = 0
        or_possede = 0
        ennemis_vaincus = []
        coffres_ouverts = []
        
        print("\nVotre aventure commence au village...")
    
    # Lancement du menu principal
    menu_principal(
        joueur=joueur,
        zone_actuelle=zone_actuelle,
        etat_quete=etat_quete,
        or_possede=or_possede,
        ennemis_vaincus=ennemis_vaincus,
        coffres_ouverts=coffres_ouverts
    )


if __name__ == "__main__":
    jeu()