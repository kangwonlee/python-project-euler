"""
Problem 004: Largest Palindrome Product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n: int) -> bool:
    """Return True if `n` is a palindrome."""
    s = str(n)
    return s == s[::-1]


def largest_palindrome_product(digits: int) -> int:
    """Return the largest palindrome made from the product of two `digits`-digit numbers."""
    low = 10 ** (digits - 1)
    high = 10 ** digits
    largest = 0
    for a in range(high - 1, low - 1, -1):
        if a * (high - 1) <= largest:
            break
        for b in range(a, low - 1, -1):
            product = a * b
            if product <= largest:
                break
            if is_palindrome(product):
                largest = product
    return largest


if __name__ == "__main__":
    print(largest_palindrome_product(3))
