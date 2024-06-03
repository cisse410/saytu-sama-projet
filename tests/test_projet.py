"""
class Projet
"""
import unittest
from datetime import datetime
from modules.membre import Membre
from modules.tache import Tache
from modules.jalon import Jalon
from modules.risque import Risque
from modules.projet import Projet


class TestProjet(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes definies
    definie dans la classe Projet
    """

    def setUp(self):
        """
        Initialisation d'un objet Projet avant chaque test
        """
        self.projet = Projet(
            nom="Projet MQPL",
            description="Gestion des projets",
            date_debut=datetime(2024, 5, 29),
            date_fin=datetime(2024, 6, 5),
        )

    def test_ajouter_tache(self):
        """
        Test de l'ajout d'une tâche
        """
        tache = Tache(
            "Analyse des besoins",
            "Analyser les besoins du client",
            datetime(2023, 1, 1),
            datetime(2023, 2, 1),
            Membre("Adama Gaye", "Testeur"),
            "En cours",
        )
        self.projet.ajouter_tache(tache)
        self.assertIn(tache, self.projet.taches)

    def test_ajouter_membre_equipe(self):
        """
        Test de l'ajout d'un membre à l'équipe
        """
        membre = Membre("Moussa KANDE", "Dev backend")
        self.projet.ajouter_membre_equipe(membre)
        self.assertIn(membre, self.projet.equipe.membres)

    def test_definir_budget(self):
        """
        Test de la définition du budget
        """
        budget = 10000.0
        self.projet.definir_budget(budget)
        self.assertEqual(self.projet.budget, budget)

    def test_ajouter_risque(self):
        """
        Test de l'ajout d'un risque
        """
        risque = Risque("Retard de livraison", 0.3, "Moyen")
        self.projet.ajouter_risque(risque)
        self.assertIn(risque, self.projet.risques)

    def test_ajouter_jalon(self):
        """
        Test de l'ajout d'un jalon
        """
        jalon = Jalon("Fin de l'analyse des besoins", datetime(2024, 6, 12))
        self.projet.ajouter_jalon(jalon)
        self.assertIn(jalon, self.projet.jalons)

    def test_enregistrer_changement(self):
        """
        Test de l'enregistrement d'un changement
        """
        description = "Changement Test"
        self.projet.enregistrer_changement(description)
        self.assertEqual(self.projet.changements[-1].description, description)
        self.assertEqual(self.projet.version, 2)

    def test_generer_rapport_performance(self):
        """
        Test de la génération du rapport de performance
        """
        rapport = self.projet.generer_rapport_performance()
        self.assertIn("Rapport de Performance du Projet", rapport)

    def test_calculer_chemin_critique(self):
        """
        Test du calcul du chemin critique
        """
        tache1 = Tache(
            "Analyse des besoins",
            "Analyser les besoins du client",
            datetime(2023, 1, 1),
            datetime(2023, 2, 1),
            Membre("Adama Gaye", "Testeur"),
            "En cours",
        )
        tache2 = Tache(
            "Développement",
            "Développer les fonctionnalités principales",
            datetime(2023, 3, 1),
            datetime(2023, 4, 1),
            Membre("Moustapha Ka", "Dev backend"),
            "Terminée",
        )
        self.projet.ajouter_tache(tache1)
        self.projet.ajouter_tache(tache2)
        self.projet.calculer_chemin_critique()
        self.assertIn(tache1, self.projet.chemin_critique)
        self.assertIn(tache2, self.projet.chemin_critique)

    def test_notifier(self):
        """
        Test de la notification
        """
        membre1 = Membre("Adama Gaye", "Testeur")
        membre2 = Membre("Moustapha ka", "Designer")
        self.projet.ajouter_membre_equipe(membre1)
        self.projet.ajouter_membre_equipe(membre2)
        message = "Message de test"
        destinataires = [membre1, membre2]
        self.projet.notifier(
            message,
            destinataires,
        )


if __name__ == "__main__":
    unittest.main()
