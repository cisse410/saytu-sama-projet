"""
Jalon
"""

import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Jalon:
    """
    Module qui permet de définir les jalons du projet
    """

    def __init__(self, nom: str, date: datetime):
        """
        Initialisation d'un jalon
        :param nom:
        :param date:
        """
        self.nom = nom
        self.date = date
