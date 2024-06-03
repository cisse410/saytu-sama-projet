"""
class TestEquipeMethods
"""

import unittest
from modules.equipe import Equipe
from modules.membre import Membre


class TestEquipeMethods(unittest.TestCase):
    """
    Cette classe permet de tester l'ensemble des methodes de classe Risque
    Dans cette etape du projet, on a que le constructeur a tester
    """

    def setUp(self):
        # Créez une équipe de test vide
        self.equipe_test = Equipe()

    def test_ajouter_membre(self):
        """
        Cette methode permet de tester la methode ajouter_membre
        :return:
        """
        # Vérifiez que la méthode ajouter_membre fonctionne correctement
        membre1 = Membre("Moussa KANE", "Lead Dev")
        membre2 = Membre("Coumba DIOUF", "Chef de projet")
        self.equipe_test.ajouter_membre(membre1)
        self.equipe_test.ajouter_membre(membre2)
        membres_obtenus = self.equipe_test.obtenir_membres()
        self.assertIn(membre1, membres_obtenus)
        self.assertIn(membre2, membres_obtenus)

    def test_obtenir_membres(self):
        """
        Cette methode permet de tester la methode obtenir_membre
        :return:
        """
        # Vérifiez que la méthode obtenir_membres renvoie la liste des membres
        membre1 = Membre("Fatou BADIANE", "Scrum Master")
        membre2 = Membre("Khadidiatou LOUM", "Dev iOS")
        membre3 = Membre("Khady KEBE", "Dev Android")
        self.equipe_test.ajouter_membre(membre1)
        self.equipe_test.ajouter_membre(membre2)
        self.equipe_test.ajouter_membre(membre3)
        membres_obtenus = self.equipe_test.obtenir_membres()
        self.assertEqual(len(membres_obtenus), 3)
        self.assertIn(membre1, membres_obtenus)
        self.assertIn(membre2, membres_obtenus)


if __name__ == "__main__":
    unittest.main()
