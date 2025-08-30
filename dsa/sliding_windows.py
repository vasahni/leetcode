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
