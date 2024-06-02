"""
Module Membre
"""

import dataclasses


@dataclasses.dataclass
class Membre:
    """
    Module permettant de definir un membre
    """

    def __init__(self, nom: str, role: str):
        self.nom = nom
        self.role = role
