"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    Takes a current board and the next player to move.
    Plays a game starting with the given player by making
    random moves, alternating between players.
    Modifies the board input.
    """
    while (board.check_win() == None):
        empty_squares = board.get_empty_squares();
        position = random.choice(empty_squares);
        board.move(position[0], position[1], player);
        player = provided.switch_player(player);
    

def mc_update_scores(scores, board, player):
    """
    takes a grid of scores (a list of lists) with the
    same dimensions as the Tic-Tac-Toe board, a board
    from a completed game, and which player the machine
    player is.
    Scores the completed board and update the scores
    grid.
    """
    dimension = board.get_dim();
    if (board.check_win() == player):
        for row in range(dimension):
            for col in range(dimension):
                if (board.square(row, col) == player):
                    scores[row][col] += SCORE_CURRENT;
                elif (board.square(row, col) == provided.switch_player(player)):
                    scores[row][col] -= SCORE_OTHER;
    elif (board.check_win() == provided.switch_player(player)):
        for row in range(dimension):
            for col in range(dimension):
                if (board.square(row, col) == player):
                    scores[row][col] -= SCORE_CURRENT;
                elif (board.square(row, col) == provided.switch_player(player)):
                    scores[row][col] += SCORE_OTHER;
    
    
def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores.
    Finds all of the empty squares with the maximum
    score and randomly return one of them as a (row,
    column) tuple.
    """
    dimension = board.get_dim();
    max_score = -2 * NTRIALS * SCORE_CURRENT;
    for row in range(dimension):
        for col in range(dimension):
            if (scores[row][col] > max_score and
                board.square(row, col) == provided.EMPTY):
                max_score = scores[row][col];
    move_pool = [];
    for row in range(dimension):
        for col in range(dimension):
            if (scores[row][col] == max_score and
                board.square(row, col) == provided.EMPTY):
                move_pool.append((row, col));
    return random.choice(move_pool);

    
def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine
    player is, and the number of trials to run.
    Use the Monte Carlo simulation described above to
    return a move for the machine player in the form
    of a (row, column) tuple.
    """
    dimension = board.get_dim();
    scores = [[0 for dummy_col in range(dimension)]
              for dummy_row in range(dimension)];
    for dummy_trial in range(trials):
        copy_board = board.clone();
        mc_trial(copy_board, player);
        mc_update_scores(scores, copy_board, player);
    return get_best_move(board, scores);

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

