# test_app.py
from app import add


def test_add():
    assert add(3, 4) == 7
    assert add(5, 5) == 10
