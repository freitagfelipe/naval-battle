import pytest
from naval_battle.model.ship.ship import Ship, Position, ShipType, ShipException
from naval_battle.DTOs.ship_dto import ShipDTO


def test_create_submarine_should_fail_with_different_positions():
    with pytest.raises(
        ShipException, match="O submarino deve começar e terminar na mesma posição"
    ):
        type = ShipType.SUBMARINE
        initial_pos = Position(10, 5)
        end_pos = Position(11, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)


def test_create_ship_should_fail_in_diagonal():
    with pytest.raises(ShipException, match="O navio não pode estar na diagonal"):
        type = ShipType.SMALL_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(11, 6)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)


def test_create_small_ship_should_fail_with_wrong_size():
    with pytest.raises(ShipException, match="O navio pequeno deve ter dois de tamanho"):
        type = ShipType.SMALL_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(12, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)

    with pytest.raises(ShipException, match="O navio pequeno deve ter dois de tamanho"):
        type = ShipType.SMALL_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(10, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)


def test_create_medium_ship_should_fail_with_wrong_size():
    with pytest.raises(ShipException, match="O navio médio deve ter três de tamanho"):
        type = ShipType.MEDIUM_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(14, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)

    with pytest.raises(ShipException, match="O navio médio deve ter três de tamanho"):
        type = ShipType.MEDIUM_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(10, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)


def test_create_big_ship_should_fail_with_wrong_size():
    with pytest.raises(
        ShipException, match="O navio grande deve ter quatro de tamanho"
    ):
        type = ShipType.BIG_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(15, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)

    with pytest.raises(
        ShipException, match="O navio grande deve ter quatro de tamanho"
    ):
        type = ShipType.BIG_SHIP
        initial_pos = Position(10, 5)
        end_pos = Position(10, 5)

        ship_dto = ShipDTO(type, initial_pos, end_pos)

        Ship(ship_dto)


def test_create_submarine_should_pass():
    type = ShipType.SUBMARINE
    initial_pos = Position(10, 5)
    end_pos = Position(10, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    Ship(ship_dto)


def test_create_small_ship_should_pass():
    type = ShipType.SMALL_SHIP
    initial_pos = Position(10, 5)
    end_pos = Position(11, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    Ship(ship_dto)


def test_create_medium_ship_should_pass():
    type = ShipType.MEDIUM_SHIP
    initial_pos = Position(10, 7)
    end_pos = Position(10, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    Ship(ship_dto)


def test_create_big_ship_should_pass():
    type = ShipType.BIG_SHIP
    initial_pos = Position(10, 5)
    end_pos = Position(13, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    Ship(ship_dto)


def test_check_type_getter():
    type = ShipType.BIG_SHIP
    initial_pos = Position(10, 5)
    end_pos = Position(13, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    ship = Ship(ship_dto)

    assert ship.type == type


def test_check_initial_pos_getter():
    type = ShipType.BIG_SHIP
    initial_pos = Position(10, 5)
    end_pos = Position(13, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    ship = Ship(ship_dto)

    assert ship.initial_pos == initial_pos


def test_check_end_pos_getter():
    type = ShipType.BIG_SHIP
    initial_pos = Position(10, 5)
    end_pos = Position(13, 5)

    ship_dto = ShipDTO(type, initial_pos, end_pos)

    ship = Ship(ship_dto)

    assert ship.end_pos == end_pos
