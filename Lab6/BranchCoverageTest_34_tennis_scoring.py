
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ================ GAME SCORE ================

def test_negative_points():
    with pytest.raises(ValueError):
        game_score(-1, 0)

    with pytest.raises(ValueError):
        game_score(0, -1)


def test_normal_scores():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 0) == "15-0"
    assert game_score(2, 1) == "30-15"
    assert game_score(3, 2) == "40-30"


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    assert game_score(3, 4) == "advantage B"


def test_game_winner_a():
    assert game_score(5, 3) == "game A"
    assert game_score(4, 2) == "game A"


def test_game_winner_b():
    assert game_score(3, 5) == "game B"
    assert game_score(2, 4) == "game B"


# ================ SET WINNER ================

def test_set_winner_a():
    assert set_winner(6, 4) == "A"


def test_set_winner_b():
    assert set_winner(4, 6) == "B"


def test_set_winner_close_scores():
    assert set_winner(6, 5) is None
    assert set_winner(5, 6) is None


def test_tiebreak_winner():
    assert set_winner(7, 6) == "A"
    assert set_winner(6, 7) == "B"


def test_tiebreak_conditions():
    assert set_winner(7, 7) is None
    assert set_winner(6, 6) is None


# ================ MATCH STATUS ================

def test_player_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_player_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_decider():
    assert match_status(1, 1, 3) == "decider"
    assert match_status(2, 2, 5) == "decider"


def test_match_in_progress():
    assert match_status(1, 0, 3) == "in progress"
    assert match_status(0, 0, 3) == "in progress"
