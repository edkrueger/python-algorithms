"""
Tests math.py.
"""
from resc.math import log_ceil_rec


def test_log_ceil_rec():
    """Tests log_cel_rec."""
    assert log_ceil_rec(32, 2) == 5
    assert log_ceil_rec(5, 2) == 3
    assert log_ceil_rec(9, 3) == 2
    assert log_ceil_rec(10, 3) == 3
