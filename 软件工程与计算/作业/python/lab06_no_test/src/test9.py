def church_to_int(n):
    """Convert the Python integer n to Church numeral.

    >>> church_to_int(0)
    zero
    >>> church_to_int(1)
    one
    >>> church_to_int(2)
    two
    >>> church_to_int(3)
    three
    """

    if n == 0:
        return zero
    else:
        return lambda f: lambda x: f(church_to_int(n - 1)(f)(x))
