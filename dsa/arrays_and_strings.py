import math


def check_palindrome(string: str) -> bool:
    """
    Example 1: Given a string s, return true if it is a palindrome, false otherwise.
    """
    string = string.lower()
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right += -1
    return True


def find_sum_sorted_array(sorted_numbers: list, expected_total: int) -> bool:
    """
    Example 2: Given a sorted array of unique integers and a target integer,
    return true if there exists a pair of numbers that sum to target, false
    otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
    """
    l = 0
    r = len(sorted_numbers) - 1
    while l < r:
        total = sorted_numbers[l] + sorted_numbers[r]
        if total == expected_total:
            return True
        elif total > expected_total:
            r -= 1
        elif total < expected_total:
            l += 1
    return False


def combine_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Example 3: Given two sorted integer arrays arr1 and arr2, return a new array
    that combines both of them and is also sorted.
    """
    i = j = 0
    combined_array = []
    while (i < len(arr1)) & (j < len(arr2)):
        if arr1[i] < arr2[j]:
            combined_array.append(arr1[i])
            i += 1
        else:
            combined_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        combined_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        combined_array.append(arr2[j])
        j += 1
    return combined_array


def reverse_string(s: list[str]) -> list[str]:
    l = 0
    r = len(s) - 1
    while l < r:
        temp = s[r]
        s[r] = s[l]
        s[l] = temp
        l += 1
        r -= 1
    return s


def sorted_squares(nums: list[int]) -> list[int]:
    l = 0
    r = len(nums) - 1
    final_array = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[l]) <= abs(nums[r]):
            final_array[i] = nums[r] * nums[r]
            r -= 1
        else:
            final_array[i] = nums[l] * nums[l]
            l += 1
    return final_array
