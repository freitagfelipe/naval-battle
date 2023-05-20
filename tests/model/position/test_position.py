from naval_battle.model.position.position import Position


def test_constructor():
    x = 10
    y = 5

    position = Position(x, y)
    expected = (x, y)

    assert position.get() == expected


def test_equal_positions_equality():
    x = 10
    y = 5

    position_one = Position(x, y)
    position_two = Position(x, y)

    assert position_one == position_two


def test_different_positions_equality():
    x_one = 10
    y_one = 5
    x_two = 20
    y_two = 15

    position_one = Position(x_one, y_one)
    position_two = Position(x_two, y_two)

    assert position_one != position_two


def test_print_position():
    assert "1,1" == str(Position(1, 1))
