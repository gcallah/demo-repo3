
import db.char_types as ctyp


def test_get_char_types():
    ct = ctyp.get_char_types()
    assert isinstance(ct, list)
    assert len(ct) > 1


def test_get_char_type_details():
    ctd = ctyp.get_char_type_details(ctyp.WARRIOR)
    assert isinstance(ctd, dict)
