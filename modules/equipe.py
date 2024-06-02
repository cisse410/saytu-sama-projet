"""
Module equipe
"""


class Equipe:
    """
    Module qui permet de définir les membres de l'équipe du projet
    """

    def __init__(self):
        """
        Initialisation  d'une equipe
        """
        self.membres = []

    def ajouter_membre(self, membre):
        """
        Methode permettant d'ajouter un membre
        :param membre:
        :return:
        """
        self.membres.append(membre)
        print(f"Email envoyé à {membre.nom}: {membre.nom} à" f" été ajoute à l'équipe")

    def obtenir_membres(self):
        """
        Methode permettant d'obtenir les memebres de l'equipe du projet
        :return:
        """
        return self.membres
