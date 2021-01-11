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
