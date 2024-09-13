# 0
class Palindrome:
    # Reference: https://leetcode.com/problems/palindrome-number/
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = self.removeNonAlNum(s)
        s_inverted = self.invertString(s)
        return s == s_inverted

    def removeNonAlNum(self, s: str) -> str:
        s_copy = s
        for char in s_copy:
            if not char.isalnum():
                s = s.replace(char, "")
        return s

    def invertString(self, s: str) -> str:
        result = ""
        for char in s:
            result = char + result
        return result


# 1
class TwoSum:
    # Reference: https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cont = 0
        for num in nums:
            remaining = target - num
            if remaining in nums:
                if cont != nums.index(remaining):
                    if cont > nums.index(remaining):
                        return [nums.index(remaining), cont]
                    else:
                        return [cont, nums.index(remaining)]
                else:
                    cont += 1
            else:
                cont += 1


# 2
# Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
def maxProfit(prices: list[int]) -> int:
    inf = 9999999999
    h1 = s1 = h2 = s2 = -inf
    for p in prices:
        s2 = max(s2, h2 + p)
        h2 = max(h2, s1 - p)
        s1 = max(s1, h1 + p)
        h1 = max(h1, -p)
    return max(0, s1, s2)


# 3
def palindrome(x: int) -> bool:
    x = str(x)
    length = len(x)
    adjustment = 0
    result = True
    if length % 2 != 0:
        adjustment = 1
    length = int(length / 2)
    for i in range(length + adjustment):
        if x[i] != x[-(i + 1)]:
            result = False
            break
    return result


# 4
# Reference: https://leetcode.com/problems/roman-to-integer/
def romanToInt(s: str):
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = s[::-1]
    cap = 0
    temp: str = s[0]
    sign = 1
    result: int = 0
    for i in s:
        if cap == 4:
            return "Numero no válido"
        if temp != i:
            if nums[temp] < nums[i]:
                sign = 1
                cap = 0
            else:
                sign = -1
            temp = i
        result += nums[i] * sign
        cap += 1
    return result


# 5
# Reference: https://leetcode.com/problems/reverse-integer/
def reverseInteger(x: int) -> int:
    sign = 1
    if x < 0:
        sign = -1
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2**31) - 1 < rst < 2**31 else 0


# 6
# Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(list1: list[int], list2: list[int]) -> float:
    total_list = list1 + list2
    total_list.sort()
    if len(total_list) % 2 == 0:
        return (
            total_list[len(total_list) // 2] + total_list[(len(total_list) // 2) - 1]
        ) / 2
    else:
        return total_list[len(total_list) // 2]


# 7
# Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s: str) -> int:
    start = maxLength = 0
    usedChar = {}
    for index, char in enumerate(s):
        if char in usedChar and start <= usedChar[char]:
            start = usedChar[char] + 1
        else:
            maxLength = max(maxLength, index - start + 1)
        usedChar[char] = index
    return maxLength


# 8
# Reference: https://leetcode.com/problems/longest-common-prefix


def Longest_Common_Prefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    minWord = min(strs, key=len)
    strs.remove(minWord)
    for cont in range(len(minWord), 0, -1):
        for word in strs:
            if not minWord == word[: len(minWord)]:
                minWord = minWord[: len(minWord) - 1]
                break
    return minWord


# 9
# Reference: https://leetcode.com/problems/detect-capital/


def detectCapitalUse(word: str) -> bool:
    if word == word.upper():
        return True
    if word == word.lower():
        return True
    if word[0] == word[0].upper() and word[1:] == word[1:].lower():
        return True
    else:
        return False


# 10
# Reference: https://leetcode.com/problems/length-of-last-word/
def lengthOfLastWord(string: str) -> int:
    words_list = string.split(" ")
    clean_words_list = []
    for item in words_list:
        if item != "":
            clean_words_list.append(item)
    clean_words_list_length = len(clean_words_list)
    return len(clean_words_list[clean_words_list_length - 1])


# 11
# Reference: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
def mergeSortedArray(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    nums1 += nums2
    nums1.sort()
    return nums1


# 12
# Reference https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1?page=1&difficulty=Basic&sortBy=submissions
def doUnion(arr1, arr2):
    result = []

    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) > 0:
            if arr1[0] not in result:
                result.append(arr1.pop(0))
            else:
                arr1.pop(0)
        if len(arr2) > 0:
            if arr2[0] not in result:
                result.append(arr2.pop(0))
            else:
                arr2.pop(0)
    return len(result)


# 13
# Reference https://www.geeksforgeeks.org/problems/third-largest-element/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions
def thirdLargest(arr):
    if len(arr) < 3:
        return -1
    else:
        arr.sort()
        return arr[len(arr) - 3]


# 14
# Reference https://www.geeksforgeeks.org/problems/find-position-of-set-bit3706/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions
def findPositionSetBit(N):
    error = -1
    binN = "{0:b}".format(N)
    binN = list(binN[::-1])
    if "1" not in binN:
        return error
    else:
        index = binN.index("1")
        binN.remove("1")
        if "1" not in binN:
            return index + 1
        else:
            return error


# 15
# Reference https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays&sortBy=submissions
def missingNumber(n, arr):
    target_set = {i for i in range(1, n + 1)}
    arr_set = set(arr)
    diff = target_set.difference(arr_set)

    return diff.pop()


# 16
# Reference https://www.geeksforgeeks.org/problems/index-of-an-extra-element/1?page=1&category=Arrays&sortBy=submissions
def findExtra(n, a, b):
    a_set, b_set = set(a), set(b)
    diff = a_set.difference(b_set)
    return a.index(diff.pop())


# 17
# Reference https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1?page=1&category=Arrays&sortBy=submissions
def transitionPoint(arr, n):
    try:
        return arr.index(1)
    except ValueError:
        return -1


# 18
# Reference https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&category=Arrays&sortBy=submissions
def arrayDuplicates(n: int, arr: list[int]) -> list[int]:
    result = []
    for i in range(0, n):
        try:
            arr.remove(i)
        except:
            continue

    result = list(set(arr))
    result.sort()
    if len(result) == 0:
        return [-1]
    return result


# 19
# Reference https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?page=1&category=Arrays&sortBy=submissions
def pushZerosToEnd(arr, n):
    non_zero_index = 0

    for i in range(n):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    while non_zero_index < n:
        arr[non_zero_index] = 0
        non_zero_index += 1

    return arr


# 20
# Reference https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1?page=1&difficulty=Basic&sortBy=submissions
def get_min_max(arr):
    max = float("-inf")
    min = float("inf")
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    return [min, max]


# 21
# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&category=Arrays&difficulty=Medium&sortBy=submissions
def majorityElement(arr):
    results = {}
    major_num = None
    pivot = float("-inf")
    for i in arr:
        if i not in results:
            results[i] = 1
        else:
            results[i] += 1
    for key in results:
        if results[key] > pivot:
            pivot = results[key]
            major_num = key
    if results[major_num] > len(arr) / 2:
        return major_num
    else:
        return -1
