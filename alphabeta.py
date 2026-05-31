import math

def alpha_beta(level, index, is_max, arr, alpha, beta):

    if level == 3:
        return arr[index]

    if is_max:
        result = -math.inf

        for child in range(2):
            score = alpha_beta(level + 1,
                               index * 2 + child,
                               False,
                               arr,
                               alpha,
                               beta)

            result = max(result, score)
            alpha = max(alpha, result)

            if alpha >= beta:
                break

        return result

    else:
        result = math.inf

        for child in range(2):
            score = alpha_beta(level + 1,
                               index * 2 + child,
                               True,
                               arr,
                               alpha,
                               beta)

            result = min(result, score)
            beta = min(beta, result)

            if alpha >= beta:
                break

        return result


leaf_nodes = [3, 5, 6, 9, 1, 2, 0, -1]

answer = alpha_beta(0, 0, True,
                    leaf_nodes,
                    -math.inf,
                    math.inf)

print("Optimal Value:", answer)
