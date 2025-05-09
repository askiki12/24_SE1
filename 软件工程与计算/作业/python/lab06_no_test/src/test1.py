print(1)
def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return (a % 2!=0) and (b % 2!=0)  # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    if n==0:
        return 1
    return n*factorial(n-1)

def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    pass  # YOUR CODE HERE
    if a<=0 or b<=0 or c<=0:
        return False
    if (a+b>c)and(a+c>b)and(b+c>a):
        return True
    return False


def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(66)
    2
    >>> number_of_six(123456)
    1
    """
    pass  # YOUR CODE HERE
    num=0
    while n!=0:
        if n%10==6:
            num=num+1
        n=n//10
    return num
    


def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    pass  # YOUR CODE HERE
    max=0
    while(n!=0):
        if(n%10>max):
            max=n%10
        n//=10
    return max
