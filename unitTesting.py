import unittest
from exercises import *
from parameterized import parameterized


class PalindromeTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/palindrome-number/
    @parameterized.expand([
        ['123321'],
        ['12321'],
        ['1']
    ])
    def test_assertTruePalindrome(self, num):
        pal = Palindrome()
        self.assertTrue(pal.isPalindrome(num))

    @parameterized.expand([
        ['123456'],
        ['123213'],
        ['98']

    ])
    def test_assertFalsePalindrome(self, num):
        pal = Palindrome()
        self.assertFalse(pal.isPalindrome(num))


class TwoSumTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/two-sum/
    @parameterized.expand([
        [[0, 1], [2, 7, 11, 15], 9],
        [[1, 2], [3, 2, 4], 6],
        [[0, 1], [3, 4], 7]

    ])
    def test_two_sum(self, result, test_list, target):
        two_sum = TwoSum()
        self.assertEqual(result, two_sum.twoSum(test_list, target))


class BestTimeToBuyTesting(unittest.TestCase):

    # Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

    @parameterized.expand([
        [6, [3, 3, 5, 0, 0, 3, 1, 4]],
        [4, [1, 2, 3, 4, 5]],
        [0, [7, 6, 4, 3, 1]],
        [0, [1]]
    ])
    def test_best_time_to_buy(self, expected, test_list):
        self.assertEqual(expected, maxProfit(test_list))


class RomanToIntTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/roman-to-integer/

    @parameterized.expand([
        [3, 'III'],
        [4, 'IV'],
        [9, 'IX'],
        [58, 'LVIII'],
        [1994, 'MCMXCIV']
    ])
    def test_romanToInt(self, decimal, roman):
        self.assertEqual(decimal, romanToInt(roman))


class ReverseIntegerTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/reverse-integer/
    @parameterized.expand([
        [321, 123],
        [-321, -123],
        [21, 120],
        [0, 0]
    ])
    def test_reverseInteger(self, expected, num):
        self.assertEqual(expected, reverseInteger(num))


class MedianSortedArrays(unittest.TestCase):
    # Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/

    @parameterized.expand([
        [2.00000, [1, 3], [2]],
        [2.50000, [1, 2], [3, 4]],
        [0.00000, [0, 0], [0, 0]],
        [1.00000, [], [1]],
        [2.00000, [2], []]
    ])
    def test_MedianSortedArray(self, result, list1, list2):
        self.assertEqual(result, findMedianSortedArrays(list1, list2))


class LengthOfLongestSubstringTesting(unittest.TestCase):

    # Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/

    @parameterized.expand([
        [3, 'abcabcbb'],
        [1, 'bbbbb'],
        [3, 'pwwkew'],
        [0, ''],
        [1, ' '],
        [2, 'aab'],
        [3, 'dvdf']
    ])
    def test_LongestSubString(self, expected, string):
        self.assertEqual(expected, lengthOfLongestSubstring(string))


class LongestCommonPrefix(unittest.TestCase):

    # Rerence: https://leetcode.com/problems/longest-common-prefix/

    @parameterized.expand([
        ['fl', ["flower", "flow", "flight"]],
        ['', ["dog", "racecar", "car"]],
        ['flower', ["flower", "flower", "flower"]],
        ['flower', ["flower", "flower", "flower", 'flowers']],
        ['', ["flower", "flower", "flower", 'notFlowers']],
        ['a', ['a']],
        ['a', ["ab", "a"]]
    ])
    def test_LongestCommonPrefix(self, expected, strs):
        self.assertEqual(expected, Longest_Common_Prefix(strs))



class DetectCapitalUse(unittest.TestCase):
    # Reference: https://leetcode.com/problems/detect-capital/

    @parameterized.expand([
        ["USA",      True],
        ["FlaG",     False],
        ["leetcode", True],
        ["Google",   True]
    ])
    def test_detectCapitalUse(self, word, result):
        self.assertEqual(result, detectCapitalUse(word))


if __name__ == '__main__':
    unittest.main()
