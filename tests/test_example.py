import pytest


def foo(x: int, y: int) -> int:
    return x + y


def bar(x: int, y: int) -> int:
    if y == 0:
        raise ZeroDivisionError

    return x // y


def test_foo():
    expected = 10

    assert foo(5, 5) == expected


def test_bar_success():
    expected = 2

    assert bar(5, 2) == 2


def test_bar_fail():
    with pytest.raises(ZeroDivisionError):
        bar(10, 0)
