
import db.games as gm


def test_get_games():
    gms = gm.get_games()
    assert isinstance(gms, list)
    assert len(gms) > 1


def test_get_game_details():
    gm_dets = gm.get_game_details(gm.TEST_GAME_NAME)
    assert isinstance(gm_dets, dict)
