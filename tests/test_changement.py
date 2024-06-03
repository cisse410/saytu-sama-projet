"""
class TestChangement
"""

import unittest
from datetime import datetime
from modules.changement import Changement


class TestChangement(unittest.TestCase):
    """
    Cette classe permet de tester l'ensemble des methodes de la classe
     TestChangement
    """

    def setUp(self):
        self.description = "Migration"
        self.version = 1
        self.date = datetime(2024, 6, 3)

    def test_changement(self):
        """
        Cette methode permet de tester l'initialisation d'une instance
        de la classe Changement
        :return:
        """

        changement = Changement(self.description, self.version, self.date)

        self.assertEqual(changement.description, self.description)
        self.assertEqual(changement.version, self.version)
        self.assertEqual(changement.date, self.date)


if __name__ == "__main__":
    unittest.main()
