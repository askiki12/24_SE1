from ADT import make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree

def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    kiki = []
    def help_oo(t):
        if is_leaf(t) and label(t) >= n:
            return 1
        if is_leaf(t):
            return 0
        res = []
        for b in branches(t):
            res += [helpo(b, n-label(t))]
        if label(t) >= n:
            return 1 + sum(res)
        return sum(res)
    for tb in branches(t):
        kiki += [bigger_path(tb, n)]
    return help_oo(t) + sum(kiki)

def helpo(t, n):
    if is_leaf(t) and label(t) >= n:
        return 1
    if is_leaf(t):
        return 0
    res = []
    for b in branches(t):
        res += [bigger_path(b, n-label(t))]
    if label(t) >= n:
        return 1 + sum(res)
    return sum(res)


t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
t2 = tree(3, [tree(4), tree(5)])
print(helpo(t,3))
print(bigger_path(t2, 3))
print(bigger_path(tree(2), 3))
