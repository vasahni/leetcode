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
