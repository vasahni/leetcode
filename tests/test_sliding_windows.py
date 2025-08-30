import pytest

from dsa.sliding_windows import flip_single_zero, subarray_highest_sum


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
