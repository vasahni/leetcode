import pytest
from dsa.arrays_and_strings import check_palindrome, combine_sorted_arrays, find_sum_sorted_array


@pytest.mark.parametrize(
    "word, expected",
    [
        ("racecar", True),
        ("madam", True),
        ("hello", False),
        ("palindrome", False),
        ("", True),
    ],
)
def test_palindrome(word, expected):
    assert check_palindrome(word) == expected


@pytest.mark.parametrize(
    "sorted_array, expected_total, exists",
    [([1, 2, 4, 6, 8, 9, 14, 15], 14, True), ([1, 2, 3, 4], 14, False), ([1, 3, 5, 6], 11, True)],
)
def test_check_for_sum(sorted_array, expected_total, exists):
    assert find_sum_sorted_array(sorted_array, expected_total) == exists


@pytest.mark.parametrize(
    "arr1, arr2, combined",
    [
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 3, 5], [2, 4, 6, 8, 9, 10], [1, 2, 3, 4, 5, 6, 8, 9, 10]),
    ],
)
def test_combine_sorted_array(arr1, arr2, combined):
    assert combine_sorted_arrays(arr1, arr2) == combined
