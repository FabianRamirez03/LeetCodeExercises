import unittest
from exercises import *
from parameterized import parameterized


class PalindromeTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/palindrome-number/
    @parameterized.expand([["123321"], ["12321"], ["1"]])
    def test_assertTruePalindrome(self, num):
        pal = Palindrome()
        self.assertTrue(pal.isPalindrome(num))

    @parameterized.expand([["123456"], ["123213"], ["98"]])
    def test_assertFalsePalindrome(self, num):
        pal = Palindrome()
        self.assertFalse(pal.isPalindrome(num))


class TwoSumTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/two-sum/
    @parameterized.expand(
        [[[0, 1], [2, 7, 11, 15], 9], [[1, 2], [3, 2, 4], 6], [[0, 1], [3, 4], 7]]
    )
    def test_two_sum(self, result, test_list, target):
        two_sum = TwoSum()
        self.assertEqual(result, two_sum.twoSum(test_list, target))


class BestTimeToBuyTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

    @parameterized.expand(
        [
            [6, [3, 3, 5, 0, 0, 3, 1, 4]],
            [4, [1, 2, 3, 4, 5]],
            [0, [7, 6, 4, 3, 1]],
            [0, [1]],
        ]
    )
    def test_best_time_to_buy(self, expected, test_list):
        self.assertEqual(expected, maxProfit(test_list))


class RomanToIntTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/roman-to-integer/

    @parameterized.expand(
        [[3, "III"], [4, "IV"], [9, "IX"], [58, "LVIII"], [1994, "MCMXCIV"]]
    )
    def test_romanToInt(self, decimal, roman):
        self.assertEqual(decimal, romanToInt(roman))


class ReverseIntegerTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/reverse-integer/
    @parameterized.expand([[321, 123], [-321, -123], [21, 120], [0, 0]])
    def test_reverseInteger(self, expected, num):
        self.assertEqual(expected, reverseInteger(num))


class MedianSortedArrays(unittest.TestCase):
    # Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/

    @parameterized.expand(
        [
            [2.00000, [1, 3], [2]],
            [2.50000, [1, 2], [3, 4]],
            [0.00000, [0, 0], [0, 0]],
            [1.00000, [], [1]],
            [2.00000, [2], []],
        ]
    )
    def test_MedianSortedArray(self, result, list1, list2):
        self.assertEqual(result, findMedianSortedArrays(list1, list2))


class LengthOfLongestSubstringTesting(unittest.TestCase):
    # Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/

    @parameterized.expand(
        [
            [3, "abcabcbb"],
            [1, "bbbbb"],
            [3, "pwwkew"],
            [0, ""],
            [1, " "],
            [2, "aab"],
            [3, "dvdf"],
        ]
    )
    def test_LongestSubString(self, expected, string):
        self.assertEqual(expected, lengthOfLongestSubstring(string))


class LongestCommonPrefix(unittest.TestCase):
    # Rerence: https://leetcode.com/problems/longest-common-prefix/

    @parameterized.expand(
        [
            ["fl", ["flower", "flow", "flight"]],
            ["", ["dog", "racecar", "car"]],
            ["flower", ["flower", "flower", "flower"]],
            ["flower", ["flower", "flower", "flower", "flowers"]],
            ["", ["flower", "flower", "flower", "notFlowers"]],
            ["a", ["a"]],
            ["a", ["ab", "a"]],
        ]
    )
    def test_LongestCommonPrefix(self, expected, strs):
        self.assertEqual(expected, Longest_Common_Prefix(strs))


class DetectCapitalUse(unittest.TestCase):
    # Reference: https://leetcode.com/problems/detect-capital/

    @parameterized.expand(
        [["USA", True], ["FlaG", False], ["leetcode", True], ["Google", True]]
    )
    def test_detectCapitalUse(self, word, result):
        self.assertEqual(result, detectCapitalUse(word))


class TestLengthOfLastWord(unittest.TestCase):
    # Reference: https://leetcode.com/problems/detect-capital/

    @parameterized.expand(
        [
            ["Hello World", 5],
            ["   fly me   to   the moon  ", 4],
            ["luffy is still joyboy", 6],
            ["                    Fabian            ", 6],
            ["                    Fabian", 6],
            ["Fabian            ", 6],
            ["    F a b i   an              ", 2],
        ]
    )
    def test_length_of_last_word(self, string, result):
        self.assertEqual(result, lengthOfLastWord(string))


class TestMergeSortedArray(unittest.TestCase):
    # Reference: https://leetcode.com/problems/detect-capital/

    @parameterized.expand(
        [
            [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
            [[1], 1, [], 0, [1]],
            [[0], 0, [1], 1, [1]],
            [[1, 6, 7], 2, [2, 4], 2, [1, 2, 4, 6]],
        ]
    )
    def test_length_of_last_word(self, nums1, nums2, m, n, result):
        self.assertEqual(result, mergeSortedArray(nums1, nums2, m, n))


class TestUnionOfTwoArrays(unittest.TestCase):
    # Reference https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1?page=1&difficulty=Basic&sortBy=submissions

    @parameterized.expand(
        [
            [[85, 25, 1, 32, 54, 6], [85, 2], 7],
            [[1, 2, 3, 4, 5], [1, 2, 3], 5],
            [[1, 2, 1, 1, 2], [2, 2, 1, 2, 1], 2],
            [[240, 96, 415], [415, 775, 215, 152, 594, 428, 908, 357, 539, 998], 12],
        ]
    )
    def test_length_of_last_word(self, nums1, nums2, result):
        self.assertEqual(result, doUnion(nums1, nums2))


class TestThirdLargest(unittest.TestCase):
    # Reference https://www.geeksforgeeks.org/problems/third-largest-element/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions

    @parameterized.expand(
        [
            [[85, 25, 1, 32, 54, 6], 32],
            [[1, 21], -1],
            [[5, 5, 5], 5],
            [[415, 775, 215, 152, 594, 428, 908, 357, 539, 998], 775],
        ]
    )
    def test_thirdLargest(self, arr, result):
        self.assertEqual(result, thirdLargest(arr))


class TestFindPositionSetBit(unittest.TestCase):
    # Reference https://www.geeksforgeeks.org/problems/third-largest-element/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions

    @parameterized.expand(
        [
            [2, 2],
            [5, -1],
        ]
    )
    def test_thirdLargest(self, arr, result):
        self.assertEqual(result, findPositionSetBit(arr))


class TestMissingNumber(unittest.TestCase):
    # Reference https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays&sortBy=submissions

    @parameterized.expand(
        [
            [5, [1, 2, 3, 5], 4],
            [2, [1], 2],
        ]
    )
    def test_MissingNumber(self, n, arr, result):
        self.assertEqual(result, missingNumber(n, arr))


class TestFindExtra(unittest.TestCase):
    # Reference https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays&sortBy=submissions

    @parameterized.expand(
        [
            [7, [2, 4, 6, 8, 9, 10, 12], [2, 4, 6, 8, 10, 12], 4],
            [6, [3, 5, 7, 8, 11, 13], [3, 5, 7, 11, 13], 3],
        ]
    )
    def test_FindExtra(self, n, a, b, result):
        self.assertEqual(result, findExtra(n, a, b))


class TestTransitionPoint(unittest.TestCase):
    # https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1?page=1&category=Arrays&sortBy=submissions

    @parameterized.expand(
        [
            [[0, 0, 0, 1, 1], 5, 3],
            [[0, 0, 0, 0], 4, -1],
        ]
    )
    def test_transitionPoint(self, arr, n, result):
        self.assertEqual(result, transitionPoint(arr, n))


class TestArrayDuplicates(unittest.TestCase):
    # https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&category=Arrays&sortBy=submissions

    @parameterized.expand(
        [
            [[0, 3, 1, 2], 4, [-1]],
            [[2, 3, 1, 2, 3], 5, [2, 3]],
        ]
    )
    def test_arrayDuplicates(self, arr, n, result):
        self.assertEqual(result, arrayDuplicates(n, arr))


class TestPushZerosToEnd(unittest.TestCase):
    # https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?page=1&category=Arrays&sortBy=submissions

    @parameterized.expand(
        [
            [[3, 5, 0, 0, 4], 5, [3, 5, 4, 0, 0]],
            [[0, 0, 0, 4], 4, [4, 0, 0, 0]],
            [[10, 2, 4], 3, [10, 2, 4]],
        ]
    )
    def test_pushZerosToEnd(self, arr, n, result):
        self.assertEqual(result, pushZerosToEnd(arr, n))


if __name__ == "__main__":
    unittest.main()
