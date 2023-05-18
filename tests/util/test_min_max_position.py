from src.model.position.position import Position
from src.util.min_max_position import min_max_position


def test_min_max_position_with_same_position():
    assert (2, 2, 2, 2) == min_max_position(Position(2, 2), Position(2, 2))


def test_min_max_position_with_different_position():
    assert (2, 2, 3, 5) == min_max_position(Position(2, 3), Position(2, 5))
