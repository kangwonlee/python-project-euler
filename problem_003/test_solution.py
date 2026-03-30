import pytest
from problem_003.solution import largest_prime_factor


def test_example():
    assert largest_prime_factor(13195) == 29


def test_answer():
    assert largest_prime_factor(600_851_475_143) == 6857


def test_prime():
    assert largest_prime_factor(17) == 17


def test_small():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(12) == 3
