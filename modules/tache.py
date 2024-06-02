"""
Module Tache
"""

import dataclasses
from datetime import datetime
from modules.membre import Membre


@dataclasses.dataclass
class Tache:
    """
    Module permettant de definir une tache
    """

    def __init__(
        self,
        nom: str,
        description: str,
        date_debut: datetime,
        date_fin: datetime,
        responsable: Membre,
        statut: str,
    ):
        """
        Initialisation d'une tache
        :param nom:
        :param description:
        :param date_debut:
        :param date_fin:
        :param responsable:
        :param statut:
        """
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances: list[Tache] = []

    def ajouter_dependance(self, tache) -> None:
        """
        Cette methode permet d'ajouter une dependance a une tache
        :param tache:
        :return:
        """
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str) -> None:
        """
        Cette methode permet de mettre a jour le statut d'une tache
        :param statut:
        :return:
        """
        self.statut = statut
