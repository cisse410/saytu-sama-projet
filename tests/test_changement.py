import unittest
from datetime import datetime
from modules.changement import Changement  

class TestChangement(unittest.TestCase):
    def setUp(self): 
        self.description = "Description 1"
        self.version = 1
        self.date = datetime(2024, 6, 3)   

    def test_changement_creation(self):
        changement = Changement(self.description, self.version, self.date)

        self.assertEqual(changement.description, self.description)
        self.assertEqual(changement.version, self.version)
        self.assertEqual(changement.date, self.date)

if __name__ == "__main__":
    unittest.main()
