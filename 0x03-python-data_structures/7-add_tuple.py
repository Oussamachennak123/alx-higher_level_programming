def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a + (0, 0)[:2-len(tuple_a)]
    c, d = tuple_b + (0, 0)[:2-len(tuple_b)]

    return (a + c, b + d)
