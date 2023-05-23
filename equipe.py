class Equipe:
    def __init__(self, nom_equipe, joueurs):
        self.nom_equipe = nom_equipe
        self.joueurs = joueurs

    def afficher_joueurs(self):
        print(f"Joueurs de l'équipe {self.nom_equipe}:")
        for joueur in self.joueurs:
            joueur.afficher_details()
            print()
