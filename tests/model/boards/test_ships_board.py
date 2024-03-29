import pytest
from naval_battle.model.boards.ship_board import ShipBoard, InvalidShip, Ship
from naval_battle.util.enums.ship_type import ShipType
from naval_battle.model.position.position import Position
from naval_battle.util.enums.cell_type import CellType
from naval_battle.DTOs.ship_dto import ShipDTO


def test_set_ship_should_fail_with_initial_x_outside_grid():
    with pytest.raises(
        InvalidShip, match="A linha da posição inicial está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(-1, 0), Position(0, 0)))

        ship_board.set_ship(ship)

    with pytest.raises(
        InvalidShip, match="A linha da posição inicial está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(10, 0), Position(9, 0)))

        ship_board.set_ship(ship)


def test_set_ship_should_fail_with_end_x_outside_grid():
    with pytest.raises(
        InvalidShip, match="A linha da posição final está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 0), Position(-1, 0)))

        ship_board.set_ship(ship)

    with pytest.raises(
        InvalidShip, match="A linha da posição final está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(9, 0), Position(10, 0)))

        ship_board.set_ship(ship)


def test_set_ship_should_fail_with_initial_y_outside_grid():
    with pytest.raises(
        InvalidShip, match="A coluna da posição inicial está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, -1), Position(0, 0)))

        ship_board.set_ship(ship)

    with pytest.raises(
        InvalidShip, match="A coluna da posição inicial está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 10), Position(0, 9)))

        ship_board.set_ship(ship)


def test_set_ship_should_fail_with_end_y_outside_grid():
    with pytest.raises(
        InvalidShip, match="A coluna da posição final está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 0), Position(0, -1)))

        ship_board.set_ship(ship)

    with pytest.raises(
        InvalidShip, match="A coluna da posição final está fora do tabuleiro"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 9), Position(0, 10)))

        ship_board.set_ship(ship)


def test_set_a_ship_should_pass():
    ship_board = ShipBoard(10, 10)

    ship = Ship(ShipDTO(ShipType.BIG_SHIP, Position(5, 5), Position(8, 5)))

    ship_board.set_ship(ship)

    for x in range(5, 9):
        assert CellType.SHIP == ship_board.grid[x][5]


def test_set_a_ship_where_already_has_a_ship_should_fail():
    with pytest.raises(InvalidShip, match="A posição já está ocupada"):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.BIG_SHIP, Position(5, 5), Position(8, 5)))

        ship_board.set_ship(ship)

        second_ship = Ship(ShipDTO(ShipType.BIG_SHIP, Position(6, 3), Position(6, 6)))

        ship_board.set_ship(second_ship)
