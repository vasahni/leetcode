import pytest
from dsa.sliding_windows import (
    flip_single_zero,
    max_average_subarray,
    max_consecutive_ones,
    max_sum_length_k,
    subarray_highest_sum,
    subarray_product_less_k,
)


@pytest.mark.parametrize(
    "arr, k, ans",
    [
        ([1, 1, 1, 3], 3, 3),
        ([3, 1, 2, 7, 4, 2, 1, 1, 5], 8, 4),
    ],
)
def test_subarray_highest_sum(arr, k, ans):
    assert subarray_highest_sum(arr, k) == ans


@pytest.mark.parametrize(
    "s, ans",
    [
        ("1101100111", 5),
    ],
)
def test_flip_single_zero(s, ans):
    assert flip_single_zero(s) == ans


@pytest.mark.parametrize(
    "arr, k, ans",
    [
        ([10, 5, 2, 6], 100, 8),
    ],
)
def test_subarray_product_less_k(arr, k, ans):
    assert subarray_product_less_k(arr, k) == ans


@pytest.mark.parametrize(
    "arr, k, ans",
    [
        ([3, -1, 4, 12, -8, 5, 6], 4, 18),
    ],
)
def test_max_sum_length_k(arr, k, ans):
    assert max_sum_length_k(arr, k) == ans


@pytest.mark.parametrize(
    "arr, k, ans",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5),
    ],
)
def test_max_average_subarray(arr, k, ans):
    assert max_average_subarray(arr, k) == ans


@pytest.mark.parametrize(
    "nums, k, ans",
    [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ],
)
def test_max_consecutive_ones(nums, k, ans):
    assert max_consecutive_ones(nums, k) == ans
