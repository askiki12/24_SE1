def missions(f):
    """DO NOT EDIT THIS FUNCTION"""
    def mission1(f):
        if f(0) == 0 and f(1) == 2:
            print('MISSION 1 SOLVED')
            return lambda g: mission2(g(f))
        else:
            print('MISSION 1 FAILED')

    def mission2(f):
        if f(0) == 0 and f(1) == 2:
            print('MISSION 2 SOLVED')
            return mission3(0, 0)
        else:
            print('MISSION 2 FAILED')

    def mission3(f, g):
        def mission3_inner(f):
            if f == g:
                return mission3(f, g + 1)

        if g == 5:
            print('MISSION 3 SOLVED')
            return 'The cake is a lie.'
        else:
            return mission3_inner

    return mission1(f)
