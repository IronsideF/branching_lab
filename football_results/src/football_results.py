


def get_result(final_score):
    if type(final_score) == dict and "home_result" in list(final_score.keys()) and "away_result" in list(final_score.keys()):
        if final_score["home_result"] > final_score["away_result"]:
            return "Home Win"
        if final_score["home_result"] < final_score["away_result"]:
            return "Away Win"
        else:
            return "Draw"
    else:
        return "Invalid input"

def get_results(final_scores):
    pass
    # (You could try and use a list comprehension for this)