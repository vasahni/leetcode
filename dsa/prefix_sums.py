"""
FORMULA:
sum(l,r) = prefix[r] - prefix[l-1]

EXAMPLE:
arr = [1,2,3,4]
prefix = [1,3,6,10]
sum(1,3) = prefix[3] - prefix[0] = 10 - 1 = 9

ALTERNATIVE:
(deals with i = 0 base case)
sum(l,r) = prefix[r] - prefix[l] + nums[l]
ex. sum(1,3) = 10 - 3 + 2 = 9

PSEUDOCODE:
prefix = [nums[0]]
for (int i = 1; i < nums.length; i++)
    prefix.append(nums[i] + prefix[prefix.length - 1])

PYTHON:
def build_prefix(nums):
    prefix = nums[0]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])

    return prefix
"""

import math


def subarray_sums(
    nums: list[int], queries: list[list], limit: int
) -> list[bool]:
    prefix = [nums[0]]
    results = []
    for num in nums[1:]:
        prefix.append(num + prefix[-1])
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        results.append(curr < limit)
    return results


def array_splits(nums: list[int]) -> int:
    prefix = [nums[0]]
    results = 0
    for num in nums[1:]:
        prefix.append(num + prefix[-1])
    for i in range(len(nums) - 1):
        left = prefix[i]
        right = prefix[-1] - prefix[i]
        if left > right:
            results += 1
    return results


def min_start_value(nums: list[int]) -> int:
    total = 0
    ans = 1
    for num in nums:
        total += num
        ans = max(ans, total * -1 + 1)
    return ans


def k_radius_subarray(nums: list[int], k: int) -> list[int]:
    prefix = [nums[0]]
    for num in nums[1:]:
        prefix.append(prefix[-1] + num)
    results = []
    for i in range(len(nums)):
        if (i + k >= len(nums)) or (i - k < 0):
            results.append(-1)
            continue
        sum = prefix[i + k] - prefix[i - k] + nums[i - k]
        results.append(math.floor(sum / (2 * k + 1)))
    return results
