"""
Tests math.py.
"""
from resc.math import (
    recursive_integer_multiplication,
    karatsuba_multiplication,
)


def test_recursive_integer_multiplication():
    """Tests test_recursive_integer_multiplication."""
    assert recursive_integer_multiplication(0, 0) == 0 * 0
    assert recursive_integer_multiplication(3, 9) == 3 * 9
    assert recursive_integer_multiplication(123, 456) == 123 * 456
    assert recursive_integer_multiplication(12, 3456) == 12 * 3456
    assert recursive_integer_multiplication(3456, 0) == 0


def test_karatsuba_multiplication():
    """Tests karatsuba_multiplication."""
    assert karatsuba_multiplication(0, 0) == 0 * 0
    assert karatsuba_multiplication(3, 9) == 3 * 9
    assert karatsuba_multiplication(123, 456) == 123 * 456
    assert karatsuba_multiplication(12, 3456) == 12 * 3456
    assert karatsuba_multiplication(3456, 0) == 0
