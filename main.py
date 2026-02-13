from personnage import Guerrier, Mage, Voleur
from lieu import Village

def choisir_classe():
    print("Choisissez votre classe :")
    print("1 - Guerrier")
    print("2 - Mage")
    print("3 - Voleur")
    
    choix = input("> ")
    
    if choix == "1":
        return Guerrier()
    elif choix == "2":
        return Mage()
    elif choix == "3":
        return Voleur()
    else:
        print("Choix invalide, par défaut Guerrier")
        return Guerrier()

def jeu():
    joueur = choisir_classe()
    village = Village(joueur, magasin=None)
    foret = village.quitterVillage()
    
    while True:
        print("\nQue voulez-vous faire ?")
        print("1 - Explorer la forêt")
        print("2 - Retourner au village")
        print("3 - Entrer dans le donjon (si clé)")
        choix = input("> ")

if __name__ == "__main__":
    jeu()