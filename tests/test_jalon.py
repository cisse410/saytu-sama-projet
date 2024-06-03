"""
class TestJalon
"""
import unittest
from datetime import datetime
from modules.jalon import Jalon


class TestJalon(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes definies
    definie dans la classe Jalon
    """
    def setUp(self):
        self.nom = "Jalonnnnn"
        self.date = datetime(2024, 6, 3)

    def test_creation_jalon(self):
        """
        Cette methode permet de tester l'initialisation d'une instance
        de la classe Changement
        :return:
        """
        jalon = Jalon(self.nom, self.date)

        self.assertEqual(jalon.nom, self.nom)
        self.assertEqual(jalon.date, self.date)


if __name__ == "__main__":
    unittest.main()
