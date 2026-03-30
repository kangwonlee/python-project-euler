import pytest
from problem_001.solution import sum_multiples


def test_example():
    assert sum_multiples(10) == 23


def test_answer():
    assert sum_multiples(1000) == 233168


def test_zero_limit():
    assert sum_multiples(0) == 0


def test_small_limits():
    assert sum_multiples(1) == 0
    assert sum_multiples(3) == 0
    assert sum_multiples(4) == 3
    assert sum_multiples(6) == 8
