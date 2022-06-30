def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    output = []
    if type(scores) == list:
        while len(output) < 3 and len(scores) > 0:
            high = max(scores)
            scores.remove(high)
            output.append(high)
        return output
    else:
        return "Invalid input"

def scores_high_to_low(scores):
    return sorted(scores, reverse=True)

