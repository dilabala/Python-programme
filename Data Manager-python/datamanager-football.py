# Déclaration des variables

meilleurs_joueurs = []

# Définition de la structure

class Joueur:
    def __init__(self, nom, age, taille, meilleurs_buts, nationalite):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.meilleurs_buts = meilleurs_buts
        self.nationalite = nationalite

# Fonctions de l'application

def ajouter_joueur(nom, age, taille, meilleurs_buts, nationalite):
    joueur = Joueur(nom, age, taille, meilleurs_buts, nationalite)
    meilleurs_joueurs.append(joueur)
    print("Le joueur", nom, "a été ajouté à la liste des meilleurs joueurs.")

def afficher_joueurs():
    print("Liste des meilleurs joueurs :")
    for joueur in meilleurs_joueurs:
        print("Nom :", joueur.nom)
        print("Âge :", joueur.age)
        print("Taille :", joueur.taille)
        print("Nombre de meilleurs buts :", joueur.meilleurs_buts)
        print("Nationalité :", joueur.nationalite)
        print("-----------------------------")

# Fonction principale

def main():
    print("Bienvenue dans le gestionnaire des meilleurs joueurs de football")
    while True:
        print("-----------------------------")
        print("1. Ajouter un joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Quitter l'application")
        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom du joueur : ")
            age = input("Âge du joueur : ")
            taille = input("Taille du joueur : ")
            meilleurs_buts = input("Nombre de meilleurs buts du joueur : ")
            nationalite = input("Nationalité du joueur : ")
            ajouter_joueur(nom, age, taille, meilleurs_buts, nationalite)
        elif choix == "2":
            afficher_joueurs()
        elif choix == "3":
            print("Merci d'avoir utilisé le gestionnaire des meilleurs joueurs de football")
            break
        else:
            print("Choix invalide.")

# Appel de la fonction principale
main()
