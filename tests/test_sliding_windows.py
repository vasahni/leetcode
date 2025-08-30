import pytest

from dsa.sliding_windows import subarray_highest_sum


@pytest.mark.parametrize("arr, k", [([1, 1, 1, 3], 3)])
def test_subarray_highest_sum(arr, k):
    assert subarray_highest_sum(arr, k) == 3
