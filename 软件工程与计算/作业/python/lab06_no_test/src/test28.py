1+1
def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    
    >>> typed = ['I', 'have', 'begun']
    >>> prompt = ['I', 'have', 'begun', 'to', 'type']
    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
    ID: 1 Progress: 0.6
    0.6
    >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
    ID: 2 Progress: 0.2
    0.2
    >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    the_len = len(prompt)
    num = 0
    for i in range(0,len(typed)):
        if typed[i]==prompt[i]:
            num+=1
        else:
            break
    send({'id': id, 'progress': num/the_len})
    print(num/the_len)
