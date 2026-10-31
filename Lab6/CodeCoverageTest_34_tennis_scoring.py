
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------- GAME SCORE TESTS ----------------

def test_negative_points():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_normal_scores():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 0) == "15-0"
    assert game_score(2, 1) == "30-15"
    assert game_score(3, 2) == "40-30"


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_advantage():
    assert game_score(4, 3) == "advantage A"
    assert game_score(3, 4) == "advantage B"


def test_game_winner():
    assert game_score(5, 3) == "game A"
    assert game_score(3, 5) == "game B"


def test_winner_without_deuce():
    assert game_score(4, 2) == "game A"
    assert game_score(2, 4) == "game B"


# ---------------- SET WINNER TESTS ----------------

def test_set_winner_normal():
    assert set_winner(6, 4) == "A"
    assert set_winner(4, 6) == "B"


def test_set_winner_tiebreak():
    assert set_winner(7, 6) == "A"
    assert set_winner(6, 7) == "B"


def test_set_undecided():
    assert set_winner(3, 2) is None


# ---------------- MATCH STATUS TESTS ----------------

def test_match_winner():
    assert match_status(2, 0, 3) == "A wins"
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"
    assert match_status(2, 2, 5) == "decider"


def test_match_in_progress():
    assert match_status(1, 0, 3) == "in progress"
