from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    True
    """
    return (lambda f:lambda x: f(f,x))(lambda f,x:1 if x == 1 else  x*f(f,(x - 1)))
