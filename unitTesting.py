import unittest
from exercises import *


class PalindromeTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/palindrome-number/
    def test_isEvenPalindrome(self):
        pal = Palindrome()
        self.assertTrue(pal.isPalindrome('123321'))

    def test_isOddPalindrome(self):
        pal = Palindrome()
        self.assertTrue(pal.isPalindrome('12321'))

    def test_notEvenPalindrome(self):
        pal = Palindrome()
        self.assertFalse(pal.isPalindrome('123456'))

    def test_notOddPalindrome(self):
        pal = Palindrome()
        self.assertFalse(pal.isPalindrome('12345'))


class TwoSumTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/two-sum/
    def test_exampleOne(self):
        two_sum = TwoSum()
        self.assertEqual([0, 1], two_sum.twoSum([2, 7, 11, 15], 9))

    def test_exampleTwo(self):
        two_sum = TwoSum()
        self.assertEqual([1, 2], two_sum.twoSum([3, 2, 4], 6))

    def test_exampleThree(self):
        two_sum = TwoSum()
        self.assertEqual([0, 1], two_sum.twoSum([3, 4], 7))


class BestTimeToBuyTesting(unittest.TestCase):

    # Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

    def test_exampleOne(self):
        self.assertEqual(6, maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))

    def test_exampleOTwo(self):
        self.assertEqual(4, maxProfit([1, 2, 3, 4, 5]))

    def test_exampleOThree(self):
        self.assertEqual(0, maxProfit([7, 6, 4, 3, 1]))

    def test_exampleOFour(self):
        self.assertEqual(0, maxProfit([1]))


class RomanToIntTesting(unittest.TestCase):

    # Reference: https://leetcode.com/problems/roman-to-integer/

    def test_exampleOne(self):
        self.assertEqual(3, romanToInt('III'))

    def test_exampleTwo(self):
        self.assertEqual(4, romanToInt('IV'))

    def test_exampleThree(self):
        self.assertEqual(9, romanToInt('IX'))

    def test_exampleFour(self):
        self.assertEqual(58, romanToInt('LVIII'))

    def test_exampleFive(self):
        self.assertEqual(1994, romanToInt('MCMXCIV'))


class ReverseIntegerTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/reverse-integer/
    def test_exampleOne(self):
        self.assertEqual(321, reverseInteger(123))

    def test_exampleTwo(self):
        self.assertEqual(-321, reverseInteger(-123))

    def test_exampleThree(self):
        self.assertEqual(21, reverseInteger(120))

    def test_exampleFour(self):
        self.assertEqual(0, reverseInteger(0))


class MedianSortedArrays(unittest.TestCase):
    # Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/
    def test_exampleOne(self):
        self.assertEqual(2.00000, findMedianSortedArrays([1, 3], [2]))

    def test_exampleTwo(self):
        self.assertEqual(2.50000, findMedianSortedArrays([1, 2], [3, 4]))

    def test_exampleThree(self):
        self.assertEqual(0.00000, findMedianSortedArrays([0, 0], [0, 0]))

    def test_exampleFour(self):
        self.assertEqual(1.00000, findMedianSortedArrays([], [1]))

    def test_exampleFive(self):
        self.assertEqual(2.00000, findMedianSortedArrays([2], []))


if __name__ == '__main__':
    unittest.main()
