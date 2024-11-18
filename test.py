import unittest
from main import divide

class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)


    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)



if __name__ == '__main__':
    unittest.main()


