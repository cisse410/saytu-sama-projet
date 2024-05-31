from ..modules import membre
class Equipe:
    def _init_(self):
        self.membres = []

    def ajouter_membre(self, membre: membre.Membre) -> None:
        self.membres.append(membre)

    def obtenir_membres(self) -> List[membre.Membre]:
        return self.membres