import pytest

from dsa.prefix_sums import (
    array_splits,
    k_radius_subarray,
    min_start_value,
    subarray_sums,
)


@pytest.mark.parametrize(
    "nums, queries, limit, ans",
    [
        ([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13, [True, False, True]),
    ],
)
def test_subarray_sums(nums, queries, limit, ans):
    assert subarray_sums(nums, queries, limit) == ans


@pytest.mark.parametrize(
    "nums, ans",
    [
        ([10, 4, -8, 7], 2),
        ([2, 3, 1, 0], 2),
    ],
)
def test_array_splits(nums, ans):
    assert array_splits(nums) == ans


@pytest.mark.parametrize(
    "nums, ans",
    [
        ([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        ([2, 3, 5, -5, -1], 1),
    ],
)
def test_min_start_value(nums, ans):
    assert min_start_value(nums) == ans


@pytest.mark.parametrize(
    "nums, ans",
    [
        ([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        ([2, 3, 5, -5, -1], 1),
    ],
)
def test_min_start_value(nums, ans):
    assert min_start_value(nums) == ans


@pytest.mark.parametrize(
    "nums, k, ans",
    [
        ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
        ([100000], 0, [100000]),
        ([8], 100000, [-1]),
    ],
)
def test_k_radius_subarray(nums, k, ans):
    assert k_radius_subarray(nums, k) == ans
