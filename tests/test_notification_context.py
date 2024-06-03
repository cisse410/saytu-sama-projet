import unittest
from modules.membre import Membre
from modules.strategy.notification_context import NotificationContext

class TestNotificationContext(unittest.TestCase):
    def setUp(self):
        self.notification_context = NotificationContext(strategy=self.strategy)

    def test_notification_to_members(self):
        membre1 = Membre("Adama Gaye","Testeur")
        membre2 = Membre("Moustapha ka","Designer")
        message_notification = "Message de test"
        destinataires = [membre1, membre2]
        self.notification_context.notifier(message_notification, destinataires)
 
if __name__ == '__main__':
    unittest.main()
