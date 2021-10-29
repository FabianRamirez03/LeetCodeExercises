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
                s = s.replace(char, '')
        return s

    def invertString(self, s: str) -> str:
        result = ''
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
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s[::-1]
    cap = 0
    temp: str = s[0]
    sign = 1
    result: int = 0
    for i in s:
        if cap == 4:
            return 'Numero no válido'
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
    return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0


# 6
# Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(list1: list[int], list2: list[int]) -> float:
    total_list = (list1 + list2)
    total_list.sort()
    if len(total_list) % 2 == 0:
        return (total_list[len(total_list) // 2] + total_list[(len(total_list) // 2) - 1]) / 2
    else:
        return total_list[len(total_list) // 2]
