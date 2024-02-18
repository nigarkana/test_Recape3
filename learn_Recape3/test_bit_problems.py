import pytest
from .bit_problems import *

def test_bit_is_even():
    given = 14
    expected = True
    got = bit_is_even(given)
    assert got == expected


