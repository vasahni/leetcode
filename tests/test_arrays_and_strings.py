import pytest
from dsa.arrays_and_strings import check_palindrome


@pytest.mark.parametrize(
    "word, expected",
    [
        ("racecar", True),
        ("madam", True),
        ("hello", False),
        ("palindrome", False),
    ],
)
def test_palindrome(word, expected):
    assert check_palindrome(word) == expected
