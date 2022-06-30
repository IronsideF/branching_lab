import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        scores = [123, 568, 700, 350, 110]
        self.assertEqual(110, latest(scores))

    # Test personal best (the highest score in the list)
    def test_highest_score(self):
        scores = [123, 568, 700, 350, 110]
        self.assertEqual(700, personal_best(scores))


    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
