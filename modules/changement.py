"""
Changement
"""

import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Changement:
    """
    Module qui permet de définir les changements du projet
    """

    def __init__(self, description: str, version: int, date: datetime):
        """
        Contructeur
        :param description:
        :param version:
        :param date:
        """
        self.description = description
        self.version = version
        self.date = date
