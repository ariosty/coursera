"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    hand_max = hand[-1]
    scores = [0 for dummy_index in range(hand_max)]
    for num in hand:
        scores[num - 1] += num
    result = 0
    for num in scores:
        if num > result:
            result = num
    return result

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    die_result = [num + 1 for num in range(num_die_sides)]
    free_cards = gen_all_sequences(die_result, num_free_dice)
    total_score = 0
    for rolled in free_cards:
        copy = list(held_dice)
        copy.extend(rolled)
        copy.sort()
        total_score += score(copy)
    return total_score * 1.0 / len(free_cards)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer = set([()])
    for dice in hand:
        temp = set(answer)
        for hold in answer:
            hold_list = list(hold)
            hold_list.append(dice)
            temp.add(tuple(hold_list))
        answer = temp
    return answer



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    max_value = 0
    max_hold = ()
    hand_len = len(hand)
    for hold in all_holds:
        free = hand_len - len(hold)
        expected = expected_value(hold, num_die_sides, free)
        if (expected > max_value):
            max_value = expected
            max_hold = hold
    return (max_value, max_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
