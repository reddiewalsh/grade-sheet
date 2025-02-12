#!/usr/bin/python
from unittest.mock import patch, mock_open
import project as p


def test_open_gradesheet_csv(): 
    test_class = "seat,id,name,test1,test2,test3\n0,0,max score,10,10,10\n1,1234,P. I. Staker,9,5,-1"
    with patch("builtins.open", mock_open(read_data=test_class)) as mock_file:
        assert p.open_gradesheet_csv("path/to/test") == [
            {"seat": "0", "id": "0", "name": "max score", "test1": "10", "test2": "10", "test3": "10",},
            {"seat": "1", "id": "1234", "name": "P. I. Staker", "test1": "9", "test2": "5", "test3": "-1",},
        ]


def test_get_score():
    with patch("builtins.input", return_value="5"):
        score = p.get_score("test valid")
        assert score == 5
    with patch("builtins.input", side_effect=["cat", "cs50", "10", "3"]):
        score = p.get_score("test invalid input")
        assert score == 10
    with patch("builtins.input", side_effect=["7", "6", "3"]):
        score = p.get_score("test max score loop", max=5)
        assert score == 3
    with patch("builtins.input", return_value=""):
        score = p.get_score("test default", default=43)
        assert score == 43


def test_add_assignment():
    with patch("builtins.input", side_effect=["5", "10", "9", "-1"]):
        test_gradebook = p.add_assignment(test_class, "test assignment", max=10, default=6)


def test_write_gradesheet_csv(): ...
