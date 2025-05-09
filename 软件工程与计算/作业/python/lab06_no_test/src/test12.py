def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maximum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12341, 3)
    341
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if l==0:
        return 0
    i=n
    num=0
    maxi=n%10
    while i>0:
        num+=1
        i//=10
        if i%10>maxi:
            maxi=i%10
    if num<=l:
        return n
    if l==1:
        return maxi
    if(n%10>(n//10)%10):
        return max_subseq(n//10, l-1)*10+n%10
    else:
        return max_subseq(n,l-1)
