import os

from scount.sourcelines import countlines_in, REAL_LINES

SOURCE_DIR = os.path.join(os.path.dirname(__file__), "samplesources")


def test_a():
    countlines_in(SOURCE_DIR)
    all_keys = REAL_LINES.keys()
    assert "C++" in all_keys
    assert "Lua" in all_keys
    assert "Python" in all_keys
    assert 4 == REAL_LINES["C++"]
    assert 2 == REAL_LINES["Lua"]
    assert 3 == REAL_LINES["Python"]
