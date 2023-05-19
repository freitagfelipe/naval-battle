import pytest
from src.model.player.player import Player
from src.model.boards.ship_board import ShipBoard
from src.model.boards.guesses_board import GuessesBoardException, GuessesBoard
from src.model.position.position import Position
from src.util.enums.ship_type import ShipType
from src.model.ship.ship import Ship
from src.DTOs.ship_dto import ShipDTO


def test_player_make_guess_in_water_should_pass():
    player = Player("jogador", GuessesBoard(ShipBoard(10, 10)))
    old_score = player.score
    player.make_guess(Position(4, 5))

    assert old_score == player.score


def test_player_make_guess_same_position_hited_before_should_fail():
    with pytest.raises(
        GuessesBoardException, match="A posicão já foi escolhida anteriormente"
    ):
        enemy_ship_board = ShipBoard(10, 10)
        enemy_ship_board.set_ship(
            Ship(ShipDTO(ShipType.SUBMARINE, Position(5, 7), Position(5, 7)))
        )
        guesses_board = GuessesBoard(enemy_ship_board)

        player = Player("jogador", guesses_board)

        player.make_guess(Position(5, 7))
        player.make_guess(Position(5, 7))


def test_player_make_guess_in_ship_should_pass():
    enemy_ship_board = ShipBoard(10, 10)
    enemy_ship_board.set_ship(
        Ship(ShipDTO(ShipType.SUBMARINE, Position(5, 7), Position(5, 7)))
    )

    player = Player("jogador", GuessesBoard(enemy_ship_board))
    old_score = player.score

    player.make_guess(Position(5, 7))

    assert player.score - old_score == 1


def test_player_make_invalid_guess_should_fail():
    with pytest.raises(GuessesBoardException):
        player = Player("jogador", GuessesBoard(ShipBoard(10, 10)))

        player.make_guess(Position(11, 10))


def test_name_getter():
    player = Player("jogador", GuessesBoard(ShipBoard(10, 10)))

    assert "jogador" == player.name


def test_round_score_getter():
    player = Player("jogador", GuessesBoard(ShipBoard(10, 10)))

    player.set_round_score()

    assert player.round_score == 1


def test_ships_bord_getter():
    player = Player("jogador", GuessesBoard(ShipBoard(2, 2)))

    assert ShipBoard(2, 2) == player.guesses_board
