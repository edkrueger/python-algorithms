"""
Tests math.py.
"""
from resc.math import log_ceil_rec, recursive_integer_multiplication_prepadded


def test_log_ceil_rec():
    """Tests log_cel_rec."""
    assert log_ceil_rec(32, 2) == 5
    assert log_ceil_rec(5, 2) == 3
    assert log_ceil_rec(9, 3) == 2
    assert log_ceil_rec(10, 3) == 3


def test_recursive_integer_multiplication_prepadded():
    """Tests test_recursive_integer_multiplication_prepadded."""
    assert recursive_integer_multiplication_prepadded(3, 9) == 3 * 9
    assert recursive_integer_multiplication_prepadded(123, 456) == 123 * 456
