"""
class TestEmailNotificationStrategyMethods
"""

import unittest
from modules.membre import Membre
from modules.strategy.email_notification_strategy import EmailNotificationStrategy


class TestEmailNotificationStrategyMethods(unittest.TestCase):
    """
    Cette classe permet de tester l'ensemble des methodes de la classe
     EmailNotificationStrategy
    """

    def setUp(self):
        self.email_strategy = EmailNotificationStrategy()

    def test_envoyer(self):
        """
        Pour verifier que la méthode envoyer affiche correctement le message
        :return:
        """
        destinataire = Membre("Moustapha CISSE", "Chef de projet")
        message = "Nouvelle mise à jour du projet disponible !"
        self.email_strategy.envoyer(message, destinataire)


if __name__ == "__main__":
    unittest.main()
