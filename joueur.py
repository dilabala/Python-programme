class Joueur:
    def __init__(self, nom, prenom, age, taille):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille

    def afficher_details(self):
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Âge: {self.age}")
        print(f"Taille: {self.taille}")
