import pytest
from naval_battle.model.boards.guesses_board import GuessesBoard, GuessesBoardException
from naval_battle.model.boards.ship_board import ShipBoard
from naval_battle.util.enums.ship_type import ShipType
from naval_battle.model.position.position import Position
from naval_battle.model.ship.ship import Ship
from naval_battle.util.enums.guess_type import GuessType
from naval_battle.DTOs.ship_dto import ShipDTO


def test_make_guess_should_pass():
    ship_board = ShipBoard(10, 10)

    ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 2), Position(1, 2)))

    ship_board.set_ship(ship)

    guesses_board = GuessesBoard(ship_board)

    assert GuessType.HIT == guesses_board.make_guess(Position(0, 2))


def test_make_guess_that_destroy_ship():
    ship_board = ShipBoard(10, 10)

    ship = Ship(ShipDTO(ShipType.SUBMARINE, Position(0, 2), Position(0, 2)))

    ship_board.set_ship(ship)

    guesses_board = GuessesBoard(ship_board)

    assert GuessType.DESTROYED == guesses_board.make_guess(Position(0, 2))


def test_make_guess_same_position_hited_before_should_fail():
    with pytest.raises(
        GuessesBoardException, match="A posicão já foi escolhida anteriormente"
    ):
        ship_board = ShipBoard(10, 10)

        ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 2), Position(1, 2)))

        ship_board.set_ship(ship)

        guesses_board = GuessesBoard(ship_board)

        guesses_board.make_guess(Position(0, 2))
        guesses_board.make_guess(Position(0, 2))


def test_make_guess_water_position_should_pass():
    ship_board = ShipBoard(10, 10)

    ship = Ship(ShipDTO(ShipType.SMALL_SHIP, Position(0, 2), Position(1, 2)))

    ship_board.set_ship(ship)

    guesses_board = GuessesBoard(ship_board)

    assert GuessType.ERROR == guesses_board.make_guess(Position(0, 4))


def test_make_guess_with_x_outside_board_should_fail():
    with pytest.raises(
        GuessesBoardException, match="O x do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(11, 1))

    with pytest.raises(
        GuessesBoardException, match="O x do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(-1, 1))


def test_make_guess_with_y_outside_board_should_fail():
    with pytest.raises(
        GuessesBoardException, match="O y do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(1, 12))

    with pytest.raises(
        GuessesBoardException, match="O y do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(1, -1))
