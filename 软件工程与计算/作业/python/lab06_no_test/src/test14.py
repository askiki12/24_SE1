def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828

    True
    """
    "*** YOUR CODE HERE ***"
    def nummax(total,i):
        if total-i>=0:
            return nummax(total,2*i)
        return i
    def help_count(total,coin):
        if total==0:
            return 1
        if total<0 or coin==0:
            return 0
        return help_count(total,coin//2)+help_count(total-coin,coin)
    return help_count(total,nummax(total,1))
