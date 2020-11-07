import unittest
from Multiplesof3or5 import *

class test_Multiples_of_3_or_5(unittest.TestCase):
    def test_multiples_of_3(self):
        testValue = 4
        expected = 3
        self.assertN(testValue, expected)
    def test_multiples_of_5(self):
        testValue = 6
        expected = 8
        self.assertN(testValue, expected)
    def test_multiples_of_5(self):
        testValue = 6
        expected = 8
        self.assertN(testValue, expected)
    def test_multiples_of_3_or_5(self):
        testValue = 10
        expected = 23
        self.assertN(testValue, expected)
    def test_large_number_for_multiples_3_of_5(self):
        testValue = 30
        expected = 195
        self.assertN(testValue, expected)
    def test_small_than_3(self):
        testValue = 3
        expected = 0
        self.assertN(testValue, expected)
    def assertN(self, testValue, expected):
        multiplesof3or5 = Multiplesof3or5()
        number = multiplesof3or5.solution(testValue)
        self.assertEqual(expected, number)
    
if __name__ == "__main__":
    unittest.main()