"""
class TestNotificationContext
"""

import dataclasses
import unittest
from modules.membre import Membre
from modules.strategy.notification_context import NotificationContext
from modules.strategy.notification_strategy import NotificationStrategy


class TestNotificationContext(unittest.TestCase):
    """
    Cette classe permet de tester toutes les methodes de la classe NotificationContext
    """

    def setUp(self):
        @dataclasses.dataclass
        class ConcreteNotificationStrategy(NotificationStrategy):
            """
            Cette classe permet d'implementer une sous-classe concrete de NotificationStrategy
            """

            def envoyer(self, message, destinataire):
                pass

        self.strategy_strategy = ConcreteNotificationStrategy()
        self.notification_context = NotificationContext(self.strategy_strategy)

    def test_notifier(self):
        """
        Cette methode permet de tester la methode notifier de la classe NotificationContext
        :return:
        """

        destinataire1 = Membre("Adama Gaye", "Testeur")
        destinataire2 = Membre("Moustapha ka", "Designer")
        message = "Vous avez reçu une nouvelle notification"
        destinataires = [destinataire1, destinataire2]
        self.notification_context.notifier(message, destinataires)


if __name__ == "__main__":
    unittest.main()
