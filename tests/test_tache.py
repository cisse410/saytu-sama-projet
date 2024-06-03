"""
class TestTacheMethods
"""
import unittest
from datetime import datetime
from modules.membre import Membre
from modules.tache import Tache


class TestTacheMethods(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes de la classe tache
    """
    def setUp(self):
        """

        :return:
        """
        # Créez une tâche de test avec des valeurs fictives pour les attributs
        self.responsable = Membre("Aliou DIOUF", "Developer")
        self.tache_test = Tache(
            nom="Authentification",
            description="Mettre en place un systeme d'authentification pour permettre"
                        "aux utilisateurs de se connecter",
            date_debut=datetime(2024, 6, 1),
            date_fin=datetime(2024, 6, 10),
            responsable=self.responsable,
            statut="En cours",
        )

    def test_ajouter_dependance(self):
        """
        Methode de test de la methode ajouter_dependance
        :return:
        """
        # Vérifiez que la méthode ajouter_dependance fonctionne correctement
        tache_dependante = Tache(
            nom="Tâche dépendante",
            description="Ceci est une tâche dépendante",
            date_debut=datetime(2024, 6, 5),
            date_fin=datetime(2024, 6, 8),
            responsable=self.responsable,
            statut="En cours",
        )
        self.tache_test.ajouter_dependance(tache_dependante)
        self.assertIn(tache_dependante, self.tache_test.dependances)

    def test_mettre_a_jour_statut(self):
        """
        Methode de test de la methode mettre_a_jour_statut
        :return:
        """
        # Vérifiez que la méthode mettre_a_jour_statut modifie correctement le statut
        self.tache_test.mettre_a_jour_statut("Terminé")
        self.assertEqual(self.tache_test.statut, "Terminé")

    # Ajoutez d'autres méthodes de test pour couvrir les autres fonctionnalités de la classe Tache


if __name__ == "__main__":
    unittest.main()
