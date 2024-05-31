from modules.membre import Membre
class Equipe:
    def _init_(self):
        self.membres = []

    def ajouter_membre(self, membre: Membre) -> None:
        self.membres.append(membre)

    def obtenir_membres(self) -> list[Membre]:
        return self.membres