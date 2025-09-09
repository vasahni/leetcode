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
