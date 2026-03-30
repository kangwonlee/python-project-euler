import pytest
from problem_002.solution import sum_even_fibonacci


def test_small_limit():
    # Even Fibonacci numbers up to 10: 2, 8 → sum = 10
    assert sum_even_fibonacci(10) == 10


def test_answer():
    assert sum_even_fibonacci(4_000_000) == 4_613_732


def test_zero_limit():
    assert sum_even_fibonacci(0) == 0


def test_single_even_term():
    # Only even term up to 2 is 2
    assert sum_even_fibonacci(2) == 2
