"""Sorting functions."""

# pylint: disable=invalid-name


def _merge(x, y):
    """Merge two sorted listed into a sorted list."""

    merged_list = []
    i = 0
    j = 0

    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            merged_list.append(x[i])
            i += 1
        else:
            merged_list.append(y[j])
            j += 1
    while i < len(x):
        merged_list.append(x[i])
        i += 1
    while j < len(y):
        merged_list.append(y[j])
        j += 1

    return merged_list


def merge_sort(x):
    """Sort a list."""
    if len(x) <= 1:
        return x
    return _merge(merge_sort(x[0 : len(x) // 2]), merge_sort(x[len(x) // 2 :]))
