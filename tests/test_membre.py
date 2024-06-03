"""
class TestMembre
"""

import unittest
from modules.membre import Membre


class TestMembre(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes definies
    definie dans la classe Membre
    """

    def test_constructor(self):
        """
        Teste si le constructeur initialise correctement les attributs.
        """
        nom = "Abdoulaye Fall"
        role = "Dev Frontend"

        membre = Membre(nom, role)

        self.assertEqual(membre.nom, nom)
        self.assertEqual(membre.role, role)


if __name__ == "__main__":
    unittest.main()
