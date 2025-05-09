def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    >>> # You aren't expected to understand the code of this test.
    >>> # It's just here to check that definition of lambda_curry2 is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(lambda_curry2)).body[0].body]
    ['Expr', 'Return']
    """
    "*** YOUR CODE HERE ***" # REMEMBER TO REMOVE THIS LINE !!!
    return lambda func:lambda x:lambda y:func(x,y)
from operator import add, mul, mod
curried_add = lambda_curry2(add)
add_three = curried_add(3)
add_three(5)
