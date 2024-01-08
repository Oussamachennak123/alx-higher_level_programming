#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Return the integer addition of a and b

    Float arguments are typecasted to ints before addition is performed

    Raises:
        TypeError: If either of a or b is a non-integer and non-float
    Usage:
    >>> add_integer(2, 98)
    100
    >>> add_integer(2.3, 98)
    100
    >>> add_integer("2", 98)
    100
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    b = int(b)
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
