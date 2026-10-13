from Math import *
import unittest

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
            self.assertEqual(multiply(2, 3), 8)
    
    def test_divide(self):
            self.assertRaises(ValueError, divide, 10, 2)
    
if __name__ == "__main__":
      unittest.main()    