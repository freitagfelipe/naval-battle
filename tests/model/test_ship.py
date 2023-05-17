from src.model.ship import Ship, Position, ShipType


def test_constructor():
    type = ShipType.SMALL_SHIP
    initial_pos = Position(10, 5)
    end_pos = Position(11, 5)

    ship = Ship(type, initial_pos, end_pos)

    assert ship.get_type() == type
    assert ship.get_initial_pos() == initial_pos
    assert ship.get_end_pos() == end_pos
