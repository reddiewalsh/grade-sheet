#!/usr/bin/python
from unittest.mock import patch
import project as p


def test_open_gradesheet_csv(): ...


def test_get_score():
    with patch("builtins.input", return_value="5"):
        score = p.get_score("test valid")
        assert score == 5
    with patch("builtins.input", side_effect=["cat", "cs50", "10", 3]):
        score = p.get_score("test invalid input")
        assert score == 10
    with patch("builtins.input", side_effect=[7, 6, 3]):
        score = p.get_score("test max score loop", max=5)
        assert score == 3
    with patch("builtins.input", return_value=""):
        score = p.get_score("test default", default=43)
        assert score == 43


def test_add_assignment():
    with patch("builtins.input", side_effect=[]):
        ...


def test_write_gradesheet_csv(): ...
