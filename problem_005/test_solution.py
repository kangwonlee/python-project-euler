import pytest
from problem_005.solution import smallest_multiple


def test_example():
    assert smallest_multiple(10) == 2520


def test_answer():
    assert smallest_multiple(20) == 232_792_560


def test_small():
    assert smallest_multiple(1) == 1
    assert smallest_multiple(2) == 2
    assert smallest_multiple(3) == 6
