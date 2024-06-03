"""
class TestSMSNotificationStrategyMethods
"""
import unittest
from modules.membre import Membre
from modules.strategy.sms_notification_strategy import SMSNotificationStrategy


class TestSMSNotificationStrategyMethods(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes definies
    definie dans la classe SMSNotificationStrategy
    """
    def setUp(self):
        self.sms_strategy = SMSNotificationStrategy()

    def test_envoyer(self):
        """
        Cette methode permet de tester la methode envoyer
        :return:
        """
        destinataire = Membre("Khady GOUMBALA", "Testeur")
        message = "Nouvelle mise à jour du projet disponible !"
        self.sms_strategy.envoyer(message, destinataire)
        # Vous pouvez ajouter d'autres assertions ici pour vérifier le comportement attendu


if __name__ == "__main__":
    unittest.main()
