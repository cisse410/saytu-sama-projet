

class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)
        print(f"Email envoyé à {membre.nom}: {membre.nom} à été ajoute à l'équipe")

    def obtenir_membres(self):
        return self.membres
