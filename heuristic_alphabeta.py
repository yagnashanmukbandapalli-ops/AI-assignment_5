import math

game_board = [
    'X', 'X', ' ',
    'O', ' ', ' ',
    ' ', 'O', ' '
]

def board_score(state):
    points = 0

    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for group in win_lines:
        cells = [state[pos] for pos in group]

        if cells.count('X') == 2 and cells.count(' ') == 1:
            points += 10

        elif cells.count('O') == 2 and cells.count(' ') == 1:
            points -= 10

    return points


def alpha_beta_search(state, level, alpha, beta, is_max):

    if level == 0:
        return board_score(state)

    if is_max:
        value = -math.inf

        for pos in range(len(state)):
            if state[pos] == ' ':
                state[pos] = 'X'

                value = max(
                    value,
                    alpha_beta_search(
                        state, level - 1,
                        alpha, beta, False
                    )
                )

                state[pos] = ' '
                alpha = max(alpha, value)

                if alpha >= beta:
                    break

        return value

    else:
        value = math.inf

        for pos in range(len(state)):
            if state[pos] == ' ':
                state[pos] = 'O'

                value = min(
                    value,
                    alpha_beta_search(
                        state, level - 1,
                        alpha, beta, True
                    )
                )

                state[pos] = ' '
                beta = min(beta, value)

                if alpha >= beta:
                    break

        return value


print(
    "Heuristic Score:",
    alpha_beta_search(
        game_board, 3,
        -math.inf, math.inf,
        True
    )
)
