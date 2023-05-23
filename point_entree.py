from joueur import Joueur
from equipe import Equipe
from ligue import Ligue

# Création des joueurs
joueur1 = Joueur("Messi", "Lionel", 34, 170)
joueur2 = Joueur("Ronaldo", "Cristiano", 36, 187)
joueur3 = Joueur("Neymar", "Jr.", 29, 175)

# Création des équipes
equipe1 = Equipe("FC Barcelone", [joueur1])
equipe2 = Equipe("Juventus", [joueur2])
equipe3 = Equipe("Paris Saint-Germain", [joueur3])

# Création de la ligue
ligue1 = Ligue("Ligue 1", [equipe1, equipe3])
ligue2 = Ligue("Serie A", [equipe2])

# Affichage des équipes et joueurs
ligue1.afficher_equipes()
ligue2.afficher_equipes()
