def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    True
    """
    "*** YOUR CODE HERE ***"
    if n==0:
        return 0
    if n%10-(n//10)%10>0:
        return n%10-(n//10)%10-1+missing_digits(n//10)
    return missing_digits(n//10)
