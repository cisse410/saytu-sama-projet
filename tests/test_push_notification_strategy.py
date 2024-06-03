"""
class PushNotificationStrategy
"""

import unittest
from modules.membre import Membre
from modules.strategy.push_notification_strategy import PushNotificationStrategy


class TestPushNotificationStrategy(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes definies
    definie dans la classe PushNotificationStrategy
    """

    def setUp(self):
        self.membre_test = Membre("Amadou Dieng", "Dev")
        self.push_strategy = PushNotificationStrategy()

    def test_envoyer(self):
        """
        Cette methode permet de tester la methode envoyer
        :return:
        """
        message = "Bonjour, ceci est un test de notification push."
        self.push_strategy.envoyer(message, self.membre_test)


if __name__ == "__main__":
    unittest.main()
