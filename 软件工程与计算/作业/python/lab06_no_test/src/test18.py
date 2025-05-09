from dice import six_sided, four_sided, make_test_dice

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

def roll_dice(current_score, num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. Besides that, for each dice
    whose outcome has same parity with player's current score, add 1 extra point.

    current_score:  The total score of the current player.
    num_rolls:      The number of dice rolls that will be made.
    dice:           A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that current_score and num_rolls is valid.
    assert type(current_score) == int, 'current_score must be an integer.'
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    current_score=0
    for i in range(0,num_rolls):
        thenum=dice()
        if thenum==1:
            return 1
        current_score+=thenum
        if current_score==2*thenum:
            current_score+=1
    return current_score
