"""
class NotificationStrategy
"""

import dataclasses
import unittest
from modules.membre import Membre
from modules.strategy.notification_strategy import NotificationStrategy


class TestNotificationStrategy(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes de la classe NotificationStrategy
    """

    def setUp(self):
        self.destinataire = Membre("Khadija Mbaye", "Analyst")

    def test_envoyer(self):
        """
        Cette methode permet de tester la methode envoyer
        :return:
        """

        @dataclasses.dataclass
        class ConcreteNotificationStrategy(NotificationStrategy):
            """
            Cette classe permet d'implementer une sous-classe concrete de NotificationStrategy
            """

            def envoyer(self, message, destinataire):
                pass

        strategy = ConcreteNotificationStrategy()
        strategy.envoyer("Vous avez reçu une nouvelle notification", self.destinataire)


if __name__ == "__main__":
    unittest.main()
