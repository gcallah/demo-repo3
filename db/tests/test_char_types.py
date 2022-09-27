
import db.char_types as ctyp


def test_get_char_types():
    assert isinstance(ctyp.get_char_types(), list)
