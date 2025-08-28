import math


def check_palindrome(string: str) -> bool:
    string = string.lower()
    left = 0
    while left < int(math.floor(len(string) / 2)):
        right = (left * -1) - 1
        if string[left] != string[right]:
            return False
        left += 1
    return True
