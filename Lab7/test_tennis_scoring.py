from hypothesis import given, strategies as st
from tennis_scoring import parse_score, game_lead, set_spread


@given(st.one_of(st.text(), st.none()))
def test_parse_score_no_crash(s):
    try:
        result = parse_score(s)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert all(isinstance(x, int) and x >= 0 for x in result)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_game_lead_no_crash(s):
    try:
        result = game_lead(s)
        assert isinstance(result, int)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_set_spread_no_crash(s):
    try:
        result = set_spread(s)
        assert isinstance(result, int)
        assert result >= 0
    except ValueError:
        pass


# Valid input tests
def test_parse_score_valid():
    assert parse_score("3-2") == (3, 2)


def test_game_lead_valid():
    assert game_lead("40-30") == 1


def test_set_spread_valid():
    assert set_spread("6,4,7") == 3
