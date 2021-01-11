"""Math Utilities."""

# pylint: disable=invalid-name
# pylint: disable=too-many-locals


def recursive_integer_multiplication(x, y):
    """Takes two positive integers and finds their product."""

    x_str = str(x)
    y_str = str(y)

    len_x = len(x_str)
    len_y = len(y_str)

    if len_x == 1 and len_y == 1:
        return x * y

    # disabled because lack of walrus suport
    # pylint: disable=used-before-assignment
    n = len_max if (len_max := max(len_x, len_y)) % 2 == 0 else len_max + 1

    x_str_padded = (n - len_x) * "0" + x_str
    y_str_padded = (n - len_y) * "0" + y_str

    a = int(x_str_padded[0 : n // 2])
    b = int(x_str_padded[n // 2 :])
    c = int(y_str_padded[0 : n // 2])
    d = int(y_str_padded[n // 2 :])

    ad = recursive_integer_multiplication(a, d)
    bc = recursive_integer_multiplication(b, c)
    ac = recursive_integer_multiplication(a, c)
    bd = recursive_integer_multiplication(b, d)

    return (10 ** n) * ac + (10 ** (n // 2)) * (ad + bc) + bd


def karatsuba_multiplication(x, y):
    """Takes two positive integers and finds their product."""

    x_str = str(x)
    y_str = str(y)

    len_x = len(x_str)
    len_y = len(y_str)

    if len_x == 1 and len_y == 1:
        return x * y

    # disabled because lack of walrus suport
    # pylint: disable=used-before-assignment
    n = len_max if (len_max := max(len_x, len_y)) % 2 == 0 else len_max + 1

    x_str_padded = (n - len_x) * "0" + x_str
    y_str_padded = (n - len_y) * "0" + y_str

    a = int(x_str_padded[0 : n // 2])
    b = int(x_str_padded[n // 2 :])
    c = int(y_str_padded[0 : n // 2])
    d = int(y_str_padded[n // 2 :])

    pq = recursive_integer_multiplication(a + b, c + d)
    ac = recursive_integer_multiplication(a, c)
    bd = recursive_integer_multiplication(b, d)

    return (10 ** n) * ac + (10 ** (n // 2)) * (pq - ac - bd) + bd


# def karatsuba_multiplication(x, y):
#     """Takes two positive integers and finds their product."""

#     x = [int(e) for e in list(str(x))]
#     y = [int(e) for e in list(str(y))]

#     if len(x) == 1:
#         return x[0] * y[0]

#     if len(x) % 2 != 0:
#         x = [0] + x
#     if len(y) % 2 != 0:
#         y = [0] + y

#     n = len(x)

#     a = int("".join([str(e) for e in x[0 : n // 2]]))
#     b = int("".join([str(e) for e in x[n // 2 :]]))
#     c = int("".join([str(e) for e in y[0 : n // 2]]))
#     d = int("".join([str(e) for e in y[n // 2 :]]))


def _log_ceil_rec(n, base):
    """Returns the number of times base divides n."""
    return 0 if n < base else 1 + _log_ceil_rec(n // base, base)


def log_ceil_rec(n, base):
    """Returns the ceiling of the log with base base of an integer n."""
    # disabled because lack of walrus suport
    # pylint: disable=used-before-assignment
    return log if base ** (log := _log_ceil_rec(n, base)) == n else log + 1


def _prep_integer_lists(x, y):
    x = [int(e) for e in list(str(x))]
    y = [int(e) for e in list(str(y))]

    len_x = len(x)
    len_y = len(y)
    max_len = max(len_x, len_y)

    log_ceil = log_ceil_rec(max_len, 2)
    len_padded = 2 ** log_ceil

    x_padded = (len_padded - len_x) * [0] + x
    y_padded = (len_padded - len_y) * [0] + y

    return x_padded, y_padded


def _recursive_integer_multiplication_prepadded(x, y):
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

    ac = _recursive_integer_multiplication_prepadded(a, c)
    ad = _recursive_integer_multiplication_prepadded(a, d)
    bc = _recursive_integer_multiplication_prepadded(b, c)
    bd = _recursive_integer_multiplication_prepadded(b, d)

    return (10 ** n) * ac + (10 ** (n // 2)) * (ad + bc) + bd


def recursive_integer_multiplication_prepadded(x, y):
    """Takes two positive integers and returns their product."""
    return _recursive_integer_multiplication_prepadded(*_prep_integer_lists(x, y))
