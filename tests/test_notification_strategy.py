import unittest
from modules.membre import Membre
from modules.strategy.notification_strategy import NotificationStrategy  # Assurez-vous d'importer correctement votre module

class TestNotificationStrategy(unittest.TestCase):
    def setUp(self): 
        self.destinataire = Membre("Khadija Mbaye","Analyst") 

    def test_envoyer(self):  
        strategy = NotificationStrategy()
 
        strategy.test_envoyer("Bonjour ", self.destinataire)

if __name__ == "__main__":
    unittest.main()
