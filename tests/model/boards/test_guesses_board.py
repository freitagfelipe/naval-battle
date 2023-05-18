import pytest
from src.model.boards.guesses_board import GuessesBoard, GuessesBoardException
from src.model.boards.ships_board import ShipBoard
from src.model.enums.ship_type import ShipType
from src.model.position.position import Position
from src.model.ship.ship import Ship
from src.model.enums.guess_type import GuessType


def test_make_guess_should_pass():
    ships_board = ShipBoard(10, 10)

    ship = Ship(ShipType.SMALL_SHIP, Position(0, 2), Position(1, 2))

    ships_board.set_ship(ship)

    guesses_board = GuessesBoard(ships_board)

    assert GuessType.HIT == guesses_board.make_guess(Position(0, 2))
    
def test_make_guess_that_destroy_ship():
    ships_board = ShipBoard(10, 10)

    ship = Ship(ShipType.SUBMARINE, Position(0, 2), Position(0, 2))

    ships_board.set_ship(ship)

    guesses_board = GuessesBoard(ships_board)

    assert GuessType.DESTROYED == guesses_board.make_guess(Position(0, 2))


def test_make_guess_same_position_hited_before_should_fail():
    with pytest.raises(
        GuessesBoardException, match="A posicão já foi escolhida anteriormente"
    ):
        ships_board = ShipBoard(10, 10)

        ship = Ship(ShipType.SMALL_SHIP, Position(0, 2), Position(1, 2))

        ships_board.set_ship(ship)

        guesses_board = GuessesBoard(ships_board)

        guesses_board.make_guess(Position(0, 2))
        guesses_board.make_guess(Position(0, 2))


def test_make_guess_water_position_should_pass():
    ships_board = ShipBoard(10, 10)

    ship = Ship(ShipType.SMALL_SHIP, Position(0, 2), Position(1, 2))

    ships_board.set_ship(ship)

    guesses_board = GuessesBoard(ships_board)

    assert GuessType.ERROR == guesses_board.make_guess(Position(0, 4))


def test_make_guess_with_x_outside_board_should_fail():
    with pytest.raises(
        GuessesBoardException, match="A linha do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(11, 1))

    with pytest.raises(
        GuessesBoardException, match="A linha do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(-1, 1))


def test_make_guess_with_y_outside_board_should_fail():
    with pytest.raises(
        GuessesBoardException, match="A coluna do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(1, 12))

    with pytest.raises(
        GuessesBoardException, match="A coluna do palpite está fora do board"
    ):
        guesses_board = GuessesBoard(ShipBoard(10, 10))

        guesses_board.make_guess(Position(1, -1))
