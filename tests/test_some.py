import os

from scount.sourcelines import countlines_in

SOURCE_DIR = os.path.join(os.path.dirname(__file__), "samplesources")


def test_a():
    real_lines = {}
    countlines_in(SOURCE_DIR, real_lines)
    all_keys = real_lines.keys()
    assert "C++" in all_keys
    assert "Lua" in all_keys
    assert "Python" in all_keys
    assert 4 == real_lines["C++"]
    assert 2 == real_lines["Lua"]
    assert 3 == real_lines["Python"]
