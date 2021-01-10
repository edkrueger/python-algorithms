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


def _recursive_integer_multiplication(x, y):
    """Takes two lists of the same size of one-digit integers.
    Where the lists' length is a factor of 2.
    Where each list represents positive multidigit numbers.
    Finds their product."""

    n = len(x)

    if n == 1:
        return x[0] * y[0]

    a = x[0 : n // 2]
    b = x[n // 2 :]
    c = y[0 : n // 2]
    d = y[n // 2 :]

    ac = _recursive_integer_multiplication(a, c)
    ad = _recursive_integer_multiplication(a, d)
    bc = _recursive_integer_multiplication(b, c)
    bd = _recursive_integer_multiplication(b, d)

    return (10 ** n) * ac + (10 ** (n // 2)) * (ad + bc) + bd


def recursive_integer_multiplication(n, m):
    """Takes two positive integers and returns their product."""
    n = [int(e) for e in list(str(n))]
    m = [int(e) for e in list(str(m))]

    len_n = len(n)
    len_m = len(m)
    max_len = max(len_n, len_m)

    log_ceil = log_ceil_rec(max_len, 2)
    len_padded = 2 ** log_ceil

    n_padded = (len_padded - len_n) * [0] + n
    m_padded = (len_padded - len_m) * [0] + m

    print(n_padded, m_padded)

    return _recursive_integer_multiplication(n_padded, m_padded)
