import pytest
from problem_004.solution import is_palindrome, largest_palindrome_product


def test_is_palindrome_true():
    assert is_palindrome(9009)
    assert is_palindrome(121)
    assert is_palindrome(1)


def test_is_palindrome_false():
    assert not is_palindrome(123)
    assert not is_palindrome(10)


def test_example():
    assert largest_palindrome_product(2) == 9009


def test_answer():
    assert largest_palindrome_product(3) == 906609
