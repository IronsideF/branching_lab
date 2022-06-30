import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    
        # away_win = {
        # "home_result": 0,
        # "away_result": 1
        # }
        # draw = {
        # "home_result": 1,
        # "away_result": 1
        # }
    def test_result_home_win(self):
        home_win = {
        "home_result": 1,
        "away_result": 0
        }
        self.assertEqual("Home Win", get_result(home_win))
    def test_result_away_win(self):
        away_win = {
        "home_result": 0,
        "away_result": 1
        }
        self.assertEqual("Away Win", get_result(away_win))
    def test_result_draw(self):
        draw = {
        "home_result": 1,
        "away_result": 1
        }
        self.assertEqual("Draw", get_result(draw))
    
    def test_result_invalid(self):
        invalid = "We won"
        self.assertEqual("Invalid input", get_result(invalid))
    
    def test_result_bad_dict(self):
        bad_input = {
        "man_u_result": 3,
        "liverpool": 2
        }
        self.assertEqual("Invalid input", get_result(bad_input))

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_result_home_away_draw(self):
        results_list = [{
        "home_result": 1,
        "away_result": 0
        }, 
        {
        "home_result": 0,
        "away_result": 1
        },
        {
        "home_result": 1,
        "away_result": 1
        }]
        self.assertEqual(["Home Win", "Away Win", "Draw"], get_results(results_list))
    
    def test_results_not_list(self):
        results_list = "Man U: 4 Liverpool: 3, Everton: 7 West Ham: 2, Aston Villa: 19 Celtic: 3"
        self.assertEqual("Invalid input", get_results(results_list))

    def test_bad_dict_list(self):
        results_list_bad = [{
        "man_u_result": 3,
        "liverpool": 2
        },
        "Man U Win",
        {
        "home_result": 1,
        "away_result": 0
        }]
        self.assertEqual(["Invalid input", "Invalid input", "Home Win"], get_results(results_list_bad))
if __name__ == "__main__":
    unittest.main()
