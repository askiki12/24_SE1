kiki = 'kiki'
def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.
    
    >>> wpm("12345", 3)
    20.0
    >>> wpm("", 10)
    0.0
    >>> wpm("a b c", 20)
    3.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    thelen = len(typed)
    return (thelen/5.0)*60.0
    # END PROBLEM 4
def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.

    >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
    'cult'
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
    'cul'
    >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
    'car'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    numdiff = []
    for i in valid_words:
        numdiff.append(diff_function(user_word,i,limit))
    the_min = min(numdiff)
    if the_min > limit:
        return user_word
    return valid_words[numdiff.index(the_min)]
    # END PROBLEM 5
def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.

    >>> big_limit = 10
    >>> sphinx_swap("car", "cad", big_limit)
    1
    >>> sphinx_swap("this", "that", big_limit)
    2
    >>> sphinx_swap("one", "two", big_limit)
    3
    >>> sphinx_swap("awful", "awesome", 3) > 3
    True
    >>> sphinx_swap("awful", "awesome", 4) > 4
    True
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    # BEGIN PROBLEM 6
    num = 0
    if len(goal)==0:
        return len(start)
    if len(start)==0:
        return len(goal)
    if start[0] != goal[0]:
        return 1+sphinx_swap(start[1:],goal[1:],limit)
    return sphinx_swap(start[1:],goal[1:],limit)
    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    
    >>> big_limit = 10
    >>> feline_fixes("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> feline_fixes("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> feline_fixes("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    >>> limit = 2
    >>> feline_fixes("ckiteus", "kittens", limit) > limit
    True
    >>> sphinx_swap("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit) > limit
    True
    """
    if len(start) == 0 or len(goal) == 0:
        return abs(len(start) - len(goal))
    if start[0] == goal[0]:
        return feline_fixes(start[1:], goal[1:], limit)
    kiss1 = sphinx_swap(goal[0] + start, goal, limit)
    kiss2 = sphinx_swap(start[1:], goal, limit)
    kiss3 = sphinx_swap(start[1:], goal[1:], limit)
    theminn = min([kiss1, kiss2, kiss3])
    if theminn == kiss1:
        return 1 + feline_fixes(goal[0] + start, goal, limit)
    elif theminn == kiss2:
        return 1 + feline_fixes(start[1:], goal, limit)
    return 1 + feline_fixes(start[1:], goal[1:], limit)
