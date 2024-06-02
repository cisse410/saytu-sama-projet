"""
Module Risque
"""

import dataclasses


@dataclasses.dataclass
class Risque:
    """
    Module permettant de definir un risque lie a un projet
    """

    def __init__(self, description: str, probabilite: float, impact: str):
        """
        Initialisation
        :param description:
        :param probabilite:
        :param impact:
        """
        self.description = description
        self.probabilite = probabilite
        self.impact = impact
