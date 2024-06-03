"""
class TestRisqueMethod
"""
import unittest

from modules.risque import Risque


class TestRisqueMethod(unittest.TestCase):
    """
    Cette classe permet de tester l'ensemble des methodes de classe Risque
    Dans cette etape du projet, on a que le constructeur a tester
    """
    def setUp(self):
        """
        Methode appelee pour preparer le test
        Elle est immediatement appelee avant d'appeler la methode a tester
        :return:
        """
        # Créez un risque de test pour les attributs
        self.risque_test = Risque(
            description="Retard de livraison",
            probabilite=0.3,
            impact="Moyen",
        )

    def test_initialisation(self):
        """
        Methode de test pour le constructeur de la classe Risque
        :return:
        """
        # Ici on verifie si les attributs sont correctement initialises
        self.assertEqual(self.risque_test.description, "Retard de livraison")
        self.assertAlmostEqual(self.risque_test.probabilite, 0.3)
        self.assertEqual(self.risque_test.impact, "Moyen")


if __name__ == "__main__":
    unittest.main()
