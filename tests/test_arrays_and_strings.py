import pytest
from dsa.arrays_and_strings import (
    check_palindrome,
    combine_sorted_arrays,
    find_sum_sorted_array,
    reverse_string,
    sorted_squares,
)


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
    [
        ([1, 2, 4, 6, 8, 9, 14, 15], 14, True),
        ([1, 2, 3, 4], 14, False),
        ([1, 3, 5, 6], 11, True),
    ],
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


@pytest.mark.parametrize(
    "arr1, reversed",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        [["v", "a", "r", "u", "n"], ["n", "u", "r", "a", "v"]],
    ],
)
def test_reverse_string(arr1, reversed):
    assert reverse_string(arr1) == reversed


@pytest.mark.parametrize(
    "arr1, final",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-9, -2, 0, 2, 3], [0, 4, 4, 9, 81]),
        ([-2, -2, -2, 2, 2], [4, 4, 4, 4, 4]),
        ([5], [25]),
    ],
)
def test_sorted_squares(arr1, final):
    assert sorted_squares(arr1) == final
