import pytest

from dsa.prefix_sums import subarray_sums


@pytest.mark.parametrize(
    "nums, queries, limit, ans",
    [
        ([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13, [True, False, True]),
    ],
)
def test_subarray_sums(nums, queries, limit, ans):
    assert subarray_sums(nums, queries, limit) == ans
