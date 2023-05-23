class Ligue:
    def __init__(self, nom_ligue, equipes):
        self.nom_ligue = nom_ligue
        self.equipes = equipes

    def afficher_equipes(self):
        print(f"Équipes de la ligue {self.nom_ligue}:")
        for equipe in self.equipes:
            equipe.afficher_joueurs()
            print()
