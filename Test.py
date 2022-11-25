import unittest
from sum import sum
class Testsum(unittest.TestCase):
    def test_sum1(self):
        result = sum(4,1)
        self.assertEqual(result,5)
    def test_sum2(self):
        result = sum(2,2)
        self.assertEqual(result,4)
    def test_sum3(self):
        result = sum(7,0)
        self.assertEqual(result,7)
    def test_sum4(self):
        result = sum(7,2)
        self.assertEqual(result,4)
    def test_sum5(self):
        result = sum(6,8)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
