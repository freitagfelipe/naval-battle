from src.model.position import Position


def test_constructor():
    x = 10
    y = 5

    position = Position(x, y)
    expected = (x, y)

    assert position.get() == expected
