"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def count(board):
    """
    Returns number of X and O in board
    """
    # counter variable for counting X and O
    count_x, count_o = (0, 0)

    # looping over board to count X and O
    for i in range(3):
        for j in range(3):
            # ensure X in board and add 1 to count_x
            if board[i][j] == X:
                count_x += 1
            # ensure O in board and add 1 to count_o
            elif board[i][j] == O:
                count_o += 1

    # return counter variable
    return count_x, count_o


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # function count return two variables count_x, and count_o
    count_x, count_o = count(board)

    # empty board, X get first moves
    if count_o + count_x == 0:
        return X

    #  X is greater than O, and X + O not equals 9 ensures that next moves is O.(Assuming X always start First.)
    elif count_x > count_o and count_x + count_o != 9:
        return O

    # when X and O get equal, and their sum is less than 9, next moves is of X
    elif count_x == count_o and count_x + count_o != 9:
        return X

    # when game is over, returns X or O doesn't matter but i choose X
    elif count_x + count_o == 9:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # empty list to store tuples
    action = []

    # looping over to get empty index positions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append((i, j))

    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # deepcopy to avoid changes in original board
    board_copy = copy.deepcopy(board)

    # raise exception if action is not valid
    if not action in actions(board):
        raise Exception

    # update player on board
    else:
        move = player(board_copy)
        i, j = action
        board_copy[i][j] = move
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # loop over to find non-diagonal winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][2]
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[2][i]

    # for i in range(3):
    #     for j in range(3):
    #         if i == j:
    #             return board[i][j]
    #         elif i + j == 2:
    #             return board[i][j]

    # for diagonal winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[2][0] != EMPTY:
        return board[0][2]
    # no one wins
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # function count return two variables count_x, and count_o
    count_x, count_o = count(board)

    # game is over, returns True
    if count_x + count_o == 9 or winner(board) != None:
        return True

    # else returns False
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # x wins
    if winner(board) == X:
        return 1
    # O wins
    elif winner(board) == O:
        return -1
    # none wins or draw
    elif winner(board) == None:
        return 0
    
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # terminal board, return None
    if terminal(board):
        return None
    
    # for player X
    if player(board) == X:
        vI = -math.inf
        move = set()
        for action in actions(board):
            # function call
            v = min_value(result(board, action))
            if v > vI:
                vI = v
                move = action
    
    # for player O
    elif player(board) == O:
        vI = math.inf
        move = set()
        for action in actions(board):
            # function call
            v = max_value(result(board, action))
            if v < vI:
                vI = v
                move = action
    # return move
    return move


def max_value(board):

    # terminal window return utility
    if terminal(board): 
        return utility(board)
    v = -math.inf
    for action in actions(board):
        # function call
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):

    # terminal window return utility
    if terminal(board): 
        return utility(board)
    v = math.inf
    for action in actions(board):
        # function call
        v = min(v, max_value(result(board, action)))   
    return v

