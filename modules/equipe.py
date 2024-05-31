from modules.membre import Membre


class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres
