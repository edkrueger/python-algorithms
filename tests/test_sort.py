"""Tests sort.py."""

from resc.sort import _merge, merge_sort


def test__merge():
    """Test _merge"""
    assert _merge([1], [2]) == [1, 2]
    assert _merge([4, 5], [3, 7]) == [3, 4, 5, 7]
    assert _merge([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    assert _merge([2, 4], [1, 3, 5]) == [1, 2, 3, 4, 5]


def test_merge_sort():
    """Test merge_sort"""
    assert merge_sort([]) == []
    assert merge_sort([6]) == [6]
    assert merge_sort([1, 4, 3, 2]) == [1, 2, 3, 4]
    assert merge_sort([2, 7, 4]) == [2, 4, 7]
