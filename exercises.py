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


# 22


# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


def maximumSumSubarray(K, Arr, N):

    if K > N:

        print("invalid K")
        return -1

    # first sum

    pivot = 0

    for i in range(K):

        pivot += Arr[i]

    temp = pivot

    for i in range(K, N):

        temp += Arr[i] - Arr[i - K]

        if pivot < temp:

            pivot = temp

    return pivot


# 23


# https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1


def countDistinct(A, N, K):

    if K > N:

        print("invalid K")
        return -1

    freq_map = {}

    results = []

    window = []

    # first iteration

    for i in range(K):

        window.append(A[i])

    results.append(len(set(window)))

    for i in range(K, N):

        window.pop(0)

        window.append(A[i])

        results.append(len(set(window)))

    return results


# 24


# https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1?page=1&category=Arrays&sortBy=submissions


def maxSubArraySum(arr):

    best_sum = arr[0]

    actual_sum = arr[0]

    # Empezamos desde el segundo elemento hasta el final del arreglo

    for num in arr[1:]:

        # Decidimos si sumamos el número actual a la suma_actual o si es mejor empezar desde el número actual

        actual_sum = max(num, actual_sum + num)

        # Actualizamos mejor_suma si suma_actual es mayor

        best_sum = max(best_sum, actual_sum)

    return best_sum


# 25
# https://www.geeksforgeeks.org/problems/second-largest3735/1?page=1&difficulty=Easy&sortBy=submissions
def getSecondLargest(arr):
    result = -1
    arr.sort(reverse=True)
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < max_num:
            result = arr[i]
            break
    return result


# 26
# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&difficulty=Easy&sortBy=submissions
# The usage of max() is making to have a Big O complexity of O(n^2)
def array_leaders_first_solution(arr):
    result = []
    while len(arr) > 1:
        if arr[0] >= max(arr[1:]):
            result.append(arr[0])
        arr = arr[1:]
    result.append(arr[0])
    return result


def array_leaders(arr):
    max_right = arr[-1]
    result = []
    result.append(max_right)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_right:
            result.append(arr[i])
            max_right = arr[i]

    return result[::-1]


array_leaders([16, 17, 4, 3, 5, 2])


# 27
# # https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&difficulty=Easy&sortBy=submissions


def sort012(arr):
    count0, count1, count2 = 0, 0, 0
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    index = 0
    for _ in range(count0):
        arr[index] = 0
        index += 1
    for _ in range(count1):
        arr[index] = 1
        index += 1
    for _ in range(count2):
        arr[index] = 2
        index += 1
    return arr


# 28
# https://www.geeksforgeeks.org/problems/implement-strstr/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions
def strstr(s, x):
    len_x = len(x)
    len_s = len(s)
    i = 0
    while i + len_x <= len_s:
        if s[i : i + len_x] == x:
            return i
        i += 1
    return -1


# 28
# https://www.geeksforgeeks.org/problems/closest-number5728/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions
def closestNumber(N, M):
    lower_candidate = (N // M) * M

    upper_candidate = (N // M + 1) * M if N % M != 0 else lower_candidate

    if abs(N - lower_candidate) == abs(N - upper_candidate):
        return (
            lower_candidate
            if abs(lower_candidate) > abs(upper_candidate)
            else upper_candidate
        )
    return (
        lower_candidate
        if abs(N - lower_candidate) < abs(N - upper_candidate)
        else upper_candidate
    )


# 29
# https://www.geeksforgeeks.org/problems/remove-common-characters-and-concatenate-1587115621/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions


def concatenatedString(s1, s2):

    common_chars = set(s1).intersection(set(s2))
    result = s1 + s2
    for char in common_chars:
        result = result.replace(char, "")
    if len(result) == 0:
        return -1
    return result


# 30
# https://www.geeksforgeeks.org/problems/find-the-fine4353/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions


def totalFine(date, cars, fine):
    result = 0
    even = True
    if date % 2 == 0:
        even = False

    for i in range(0, len(cars)):
        if even:
            if cars[i] % 2 == 0:
                result += fine[i]
        else:
            if cars[i] % 2 != 0:
                result += fine[i]

    return result


# 31
# https://www.geeksforgeeks.org/problems/minimize-string-value1010/1?page=1&company=Microsoft&difficulty=Basic&sortBy=submissions


def minimizeStringValue(S, K):
    char_counts = {}
    for char in S:
        try:
            char_counts[char] += 1
        except:
            char_counts[char] = 1
    result = 0
    for _, count in char_counts.items():
        actual_count = count - K
        if actual_count < 1:
            actual_count = 1
        result += actual_count**2
    return result


# 32
"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
The number 20 has binary representation 10100 and contains one binary gap of length 1. 
The number 15 has binary representation 1111 and has no binary gaps. 
The number 32 has binary representation 100000 and has no binary gaps.
"""


def binary_gap(N):
    bin_N = bin(N)[2:]
    result = 0
    pivot = 0
    counting_zeros = False
    for bit in bin_N:
        if not counting_zeros and bit == "1":
            counting_zeros = True
            pivot = 0
        elif bit == "0":
            counting_zeros = True
            pivot += 1
        elif counting_zeros and bit == "1":
            if pivot > result:
                result = pivot
            pivot = 0
            counting_zeros = False

    return result


# 33
def first_unique_number(array):
    ocurrences = {}
    for num in array:
        if num not in ocurrences:
            ocurrences[num] = 1
        else:
            ocurrences[num] += 1

    for key, value in ocurrences.items():
        if value == 1:
            return key
    return -1


######################################################################

# 34
import re


def longest_password(passwords):
    passwords = passwords.split(" ")
    longest_valid_lenght = -1
    for password in passwords:
        if is_valid_password(password) and len(password) > longest_valid_lenght:
            longest_valid_lenght = len(password)

    return longest_valid_lenght


def is_valid_password(password):
    alphanumeric_pattern = "^[a-zA-Z0-9_]+$"
    num_pattern = "[0-9]"

    if not re.match(alphanumeric_pattern, password):
        return False

    total_num = 0
    total_letter = 0

    for char in password:
        if re.match(num_pattern, char):
            total_num += 1
        else:
            total_letter += 1

    return total_letter % 2 == 0 and total_num % 2 == 1


##################################################################

# 35
# https://app.codility.com/programmers/trainings/5/parking_bill/

import datetime


def parking_bill(E, L):
    total_time = get_total_time(E, L)
    total_seconds = total_time.seconds

    total_hours = total_seconds // 3600
    remaining_minutes = (total_seconds % 3600) // 60

    initial_fee = 2
    first_hour_fee = 3
    extra_hour_fee = 4

    # Calculating bill

    total_bill = 0

    total_bill += initial_fee

    if remaining_minutes > 0:
        total_bill += first_hour_fee
        remaining_minutes = 0
    elif total_hours >= 1:
        total_bill += first_hour_fee
        total_hours -= 1

    total_bill += extra_hour_fee * total_hours

    return total_bill


def get_total_time(E, L):
    hours_format = "%H:%M"
    enter_time = datetime.datetime.strptime(E, hours_format)
    leave_time = datetime.datetime.strptime(L, hours_format)
    total_time = leave_time - enter_time
    return total_time


# 36
# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/number-of-islands-easy


def countIslands_custom(matrix):
    islands = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 1:
                populate_islands((y, x), islands, matrix)
    print(islands)
    return len(islands)


def populate_islands(coords, islands, matrix):
    closest_neighbor = get_closest_neighbor(coords, matrix)
    print(f"coords: {coords} closest_neighbor: {closest_neighbor}")
    if closest_neighbor != -1 and len(islands) != 0:
        for i in range(len(islands)):
            if closest_neighbor in islands[i]:
                islands[i].append(coords)
                return
        islands.append([coords])

    else:
        islands.append([coords])


def get_closest_neighbor(coords, matrix):
    result = -1
    y = coords[0]
    x = coords[1]
    # Up neigboard
    try:
        if matrix[y - 1][x] == 1 and y != 0:
            result = (y - 1, x)
            return result
    except:
        pass
    # Left neigboard
    try:
        if matrix[y][x - 1] == 1 and x != 0:
            result = (y, x - 1)
            return result
    except:
        pass
    # Right neigboard
    try:
        if matrix[y][x + 1] == 1:
            result = (y, x + 1)
            return result
    except:
        pass
    # Down neigboard
    try:
        if matrix[y + 1][x] == 1:
            result = (y + 1, x)
            return result
    except:
        pass

    return result


# trying BFS approach


def count_islands(matrix):
    total_islands = 0
    rows = len(matrix)
    columns = len(matrix[0])

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 1:
                island_dfs(matrix, row, column)
                total_islands += 1
    return total_islands


def island_dfs(matrix, row, column):
    if row >= len(matrix) or row < 0 or column >= len(matrix[0]) or column < 0:
        return
    if matrix[row][column] == 0:
        return

    matrix[row][column] = 0

    # Up
    island_dfs(matrix, row - 1, column)
    # Right
    island_dfs(matrix, row, column + 1)
    # Down
    island_dfs(matrix, row + 1, column)
    # Left
    island_dfs(matrix, row, column - 1)


# 37
# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/biggest-island-easy


def biggest_island(matrix):
    biggest_island_len = 0
    rows = len(matrix)
    columns = len(matrix[0])

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 1:
                island_size = island_dfs_biggest(matrix, row, column)
                if island_size > biggest_island_len:
                    biggest_island_len = island_size
    return biggest_island_len


def island_dfs_biggest(matrix, row, column):
    if row >= len(matrix) or row < 0 or column >= len(matrix[0]) or column < 0:
        return 0
    if matrix[row][column] == 0:
        return 0

    matrix[row][column] = 0

    area = 1

    # Up
    area += island_dfs_biggest(matrix, row - 1, column)
    # Right
    area += island_dfs_biggest(matrix, row, column + 1)
    # Down
    area += island_dfs_biggest(matrix, row + 1, column)
    # Left
    area += island_dfs_biggest(matrix, row, column - 1)

    return area


# 38
# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/flood-fill-easy


def flood_fill(matrix, starting_cell, new_color):
    y = starting_cell[0]
    x = starting_cell[1]
    current_color = matrix[y][x]

    if current_color != new_color:
        flood_fill_bsf(matrix, new_color, current_color, y, x)

    return matrix


def flood_fill_bsf(matrix, new_color, current_color, y, x):
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        return
    if matrix[y][x] != current_color:
        return

    matrix[y][x] = new_color

    # Up
    flood_fill_bsf(matrix, new_color, current_color, y - 1, x)
    # Right
    flood_fill_bsf(matrix, new_color, current_color, y, x + 1)
    # Down
    flood_fill_bsf(matrix, new_color, current_color, y + 1, x)
    # Left
    flood_fill_bsf(matrix, new_color, current_color, y, x - 1)


# 39
# https://leetcode.com/problems/sign-of-the-product-of-an-array/


def arraySign(nums: list[int]) -> int:
    if len(nums) <= 1:
        if nums[0] == 0:
            return 0
        else:
            return nums[0] // abs(nums[0])
    if nums[0] == 0 or nums[1] == 0:
        return 0
    initial_sign = nums[0] * nums[1]
    result = initial_sign // abs(initial_sign)
    del initial_sign

    for num in nums[2:]:
        if num == 0:
            result = 0
            break
        elif num < 0 and result < 0:
            result = 1
        elif num > 0 and result < 0:
            result = -1
        elif num < 0 and result > 0:
            result = -1
        else:  # num > 0 and result > 0
            result = 1

    return result


"""
MostVoted Leetcode

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums: 
            if x == 0: return 0 
            if x < 0: ans *= -1
        return ans 
"""
