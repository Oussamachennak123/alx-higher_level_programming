#!/usr/bin/python3
def add_integer(a, b=98):
    """
    function that adds 2 integers
    @a: int
    @b = 98
    """
    a = int(a)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    b = int(b)
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    return (a + b)
