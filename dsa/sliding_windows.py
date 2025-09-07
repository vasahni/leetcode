"""
SLIDING WINDOW GENERATE TEMPLATE:

function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer

WHEN TO THINK ABOUT
When a problem asks you to find subarrays that are valid. E.g, find the longest
valid subarray.
"""


def subarray_highest_sum(arr: list[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(arr)):
        curr += arr[right]
        while curr > k:
            curr -= arr[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans


def flip_single_zero(s: str) -> int:
    """
    You are given a binary string s (a string containing only "0" and "1").
    You may choose up to one "0" and flip it to a "1". What is the length of
    the longest substring achievable that contains only "1"?

    Trick: what is the longest substring that contains at most one 0
    """
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


def subarray_product_less_k(nums: list[int], k: int) -> int:
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


def max_sum_length_k(arr: list[int], k: int) -> int:
    """
    Example 4: Given an integer array nums and an integer k, find the sum of
    the subarray with the largest sum whose length is k.

    At index i, want to remove k elements back. So adding nums[i], and removing
    nums[i-k]
    """
    curr = ans = 0
    for i in range(k):
        curr += arr[i]
    ans = curr
    for i in range(k, len(arr)):
        curr += arr[i]
        curr -= arr[i - k]
        ans = max(ans, curr)
    return ans


def max_average_subarray(arr: list[int], k: int) -> float:
    curr = ans = 0
    for i in range(k):
        curr += arr[i]
    ans = curr / k
    for i in range(k, len(arr)):
        curr += arr[i]
        curr -= arr[i - k]
        ans = max(ans, curr / k)
    return ans


def max_consecutive_ones(nums: list[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans
