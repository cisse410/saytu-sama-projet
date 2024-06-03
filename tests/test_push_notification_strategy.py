import unittest
from modules.membre import Membre
from modules.strategy.push_notification_strategy import PushNotificationStrategy

class TestPushNotificationStrategy(unittest.TestCase):
    def setUp(self): 
        self.membre_test = Membre("Amadou Dieng", "Dev") 
        self.push_strategy = PushNotificationStrategy()

    def test_envoyer(self): 
        message = "Bonjour, ceci est un test de notification push." 
        self.push_strategy.envoyer(message, self.membre_test)  

if __name__ == "__main__":
    unittest.main()
