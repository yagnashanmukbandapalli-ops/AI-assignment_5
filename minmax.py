import math

game_state = [' ' for _ in range(9)]

def show_board(state):
    for row in range(0, 9, 3):
        print(state[row:row + 3])

def winner(state, symbol):
    patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    return any(
        all(state[pos] == symbol for pos in pattern)
        for pattern in patterns
    )

def board_full(state):
    return ' ' not in state

def evaluate_move(state, is_max):
    if winner(state, 'X'):
        return 1

    if winner(state, 'O'):
        return -1

    if board_full(state):
        return 0

    if is_max:
        score = -math.inf

        for pos in range(9):
            if state[pos] == ' ':
                state[pos] = 'X'
                score = max(score,
                            evaluate_move(state, False))
                state[pos] = ' '

        return score

    else:
        score = math.inf

        for pos in range(9):
            if state[pos] == ' ':
                state[pos] = 'O'
                score = min(score,
                            evaluate_move(state, True))
                state[pos] = ' '

        return score

def find_best_move(state):
    highest_score = -math.inf
    best_position = -1

    for pos in range(9):
        if state[pos] == ' ':
            state[pos] = 'X'

            current_score = evaluate_move(state, False)

            state[pos] = ' '

            if current_score > highest_score:
                highest_score = current_score
                best_position = pos

    return best_position

game_state = [
    'X', 'X', ' ',
    'O', 'O', ' ',
    ' ', ' ', ' '
]

print("Best Move:", find_best_move(game_state))
