import unittest
from datetime import datetime
from modules.jalon import Jalon  

class TestJalon(unittest.TestCase):
    def setUp(self):
        self.nom = "Jalonnnnn"
        self.date = datetime(2024, 6, 3)
        
    def test_jalon_creation(self):
        jalon = Jalon(self.nom, self.date)

        self.assertEqual(jalon.nom, self.nom)
        self.assertEqual(jalon.date, self.date)

if __name__ == "__main__":
    unittest.main()
