#!/usr/bin/python
from unittest.mock import patch, mock_open
import project as p


def test_open_gradesheet_csv():
    test_class = "seat,id,name,test1,test2,test3\n0,0,max score,10,10,10\n1,1234,P. I. Staker,9,5,-1"
    with patch("builtins.open", mock_open(read_data=test_class)) as mock_file:
        assert p.open_gradesheet_csv("path/to/test") == [
            {
                "seat": "0",
                "id": "0",
                "name": "max score",
                "test1": "10",
                "test2": "10",
                "test3": "10",
            },
            {
                "seat": "1",
                "id": "1234",
                "name": "P. I. Staker",
                "test1": "9",
                "test2": "5",
                "test3": "-1",
            },
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
    test_class = [
        {"seat": "0"},
        {"seat": "1"},
        {"seat": "2"},
        {"seat": "3"},
        {"seat": "4"},
        {"seat": "5"},
    ]
    with patch("builtins.input", side_effect=["5", "10", "9", "-1", ""]):
        test_gradebook = p.add_assignment(
            test_class, "test assignment", max=10, default=6
        )
        assert test_gradebook == [
        {"seat": "0", "test assignment": 10},
        {"seat": "1", "test assignment": 5},
        {"seat": "2", "test assignment": 10},
        {"seat": "3", "test assignment": 9},
        {"seat": "4", "test assignment": -1},
        {"seat": "5", "test assignment": 6},
    ]
    with patch("builtins.input", side_effect=["45", "", "79", "49", "32", "cat", "-1"]):
        test_with_invalid_input = p.add_assignment(
            test_gradebook, "another test", max=50, default=29
        )
        assert test_with_invalid_input == [
        {"seat": "0", "test assignment": 10, "another test": 50},
        {"seat": "1", "test assignment": 5, "another test": 45},
        {"seat": "2", "test assignment": 10, "another test": 29},
        {"seat": "3", "test assignment": 9, "another test": 49},
        {"seat": "4", "test assignment": -1, "another test": 32},
        {"seat": "5", "test assignment": 6, "another test": -1},
    ]

def test_write_gradesheet_csv(): ...
