import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        result = multiply(3, 4)
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()
