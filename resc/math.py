"""Math Utilities."""

# pylint: disable=invalid-name


def _log_ceil_rec(n, base):
    """Returns the number of times base divides n."""
    return 0 if n < base else 1 + _log_ceil_rec(n // base, base)


def log_ceil_rec(n, base):
    """Returns the ceiling of the log with base base of an integer n."""
    # disabled because lack of walrus suport
    # pylint: disable=used-before-assignment
    return log if base ** (log := _log_ceil_rec(n, base)) == n else log + 1
