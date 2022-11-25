import unittest
from ncr import nCr
class TestnCr(unittest.TestCase):
    def test_nCr1(self):
        result = nCr(4,1)
        self.assertEqual(result,4)
    def test_nCr2(self):
        result = nCr(2,2)
        self.assertEqual(result,1)
    def test_nCr3(self):
        result = nCr(7,0)
        self.assertEqual(result,1)
    def test_nCr4(self):
        result = nCr(7,2)
        self.assertEqual(result,7)
    def test_nCr5(self):
        result = nCr(6,3)
        self.assertEqual(result,4)

if __name__ == '__main__':
    unittest.main()
