import unittest
from main import check

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(not check(1))
        self.assertTrue(check(2))
        self.assertTrue(not check(3))
        self.assertFalse(check(221))
        self.assertFalse(not check(220))

if __name__ == '__main__':
    unittest.main()


