import unittest

from src.high_scores import *

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
    def test_top_three(self):
        scores = [123, 568, 700, 350, 110]
        self.assertEqual([700, 568, 350], personal_top_three(scores))

    # Test ordered from highest tp lowest

    def test_high_to_low(self):
        scores = [123, 568, 700, 350, 110]
        self.assertEqual([700, 568, 350, 123, 110], scores_high_to_low(scores))

    # Test top three when there is a tie
    def test_tied_top_three(self):
        scores = [123, 568, 568, 568, 700, 350, 110]
        self.assertEqual([700, 568, 568], personal_top_three(scores))
    # Test top three when there are less than three
    def test_top_three_less_than_three(self):
        scores = [123, 568]
        self.assertEqual([568, 123], personal_top_three(scores))

    # Test top three when there is only one
    def test_top_three_only_one(self):
        scores = [123]
        self.assertEqual([123], personal_top_three(scores))

    def test_bad_input(self):
        scores = "123, 568, 700"
        self.assertEqual("Invalid input", personal_top_three(scores))