import pytest
from .bit_problems import *


def test_bit_is_even():
    given = 14
    expected = True
    got = bit_is_even(given)
    assert got == expected


def test_bit_is_odd():
    given = 13
    expected = True
    got = bit_is_odd(given)
    assert got == expected


def test_bit_is_odd():
    given = 15
    expected = True
    got = bit_is_odd1(given)
    assert got == expected
