import unittest

from Fish import Fish
from Plant import Plant

class TestAquarium(unittest.TestCase):

    def test_godfish(self):
        #Arrange 
        goldfish = Fish("Goldfish", 0)

        #Act
        goldfish.update_food_level(20)

        #Assert
        self.assertEqual(goldfish.food_level, 12)

    def test_seaweed(self):
        seaweed = Plant("Seaweed", 0)
        seaweed.update_food_level(16)
        self.assertEqual(seaweed.food_level,8)
        

if __name__ == "__main__":
    unittest.main()