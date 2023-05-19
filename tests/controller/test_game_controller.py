from src.controller.game_controller import GameController, Player, Position, GuessType, CurrentPlayer
from src.DTOs.ship_dto import ShipDTO
from src.model.boards.ship_board import ShipBoard
from src.model.ship.ship import ShipType


def test_alternate_player():
    game_controller = GameController()

    game_controller.construct_players("Felipe", "Henok")

    assert game_controller.alternate_player() == "Henok"
    assert game_controller.alternate_player() == "Felipe"


def test_compute_player_guess():
    ship_one = ShipDTO(ShipType.SUBMARINE, Position(5, 5), Position(5, 5))
    ship_two = ShipDTO(ShipType.SMALL_SHIP, Position(6, 5), Position(7, 5))

    game_controller = GameController()

    game_controller.set_player_ship(CurrentPlayer.PLAYER_ONE, ship_one)
    game_controller.set_player_ship(CurrentPlayer.PLAYER_ONE, ship_two)

    game_controller.set_player_ship(CurrentPlayer.PLAYER_TWO, ship_one)
    game_controller.set_player_ship(CurrentPlayer.PLAYER_TWO, ship_two)

    game_controller.construct_players("Felipe", "Henok")

    assert game_controller.compute_player_guess(Position(5, 5)) == GuessType.DESTROYED

    game_controller.alternate_player()

    assert game_controller.compute_player_guess(Position(6, 5)) == GuessType.HIT

    game_controller.alternate_player()

    assert game_controller.compute_player_guess(Position(3, 3)) == GuessType.ERROR


def test_get_player_score():
    ship_one = ShipDTO(ShipType.SUBMARINE, Position(5, 5), Position(5, 5))
    ship_two = ShipDTO(ShipType.SMALL_SHIP, Position(6, 5), Position(7, 5))

    game_controller = GameController()

    game_controller.set_player_ship(CurrentPlayer.PLAYER_ONE, ship_one)
    game_controller.set_player_ship(CurrentPlayer.PLAYER_ONE, ship_two)

    game_controller.set_player_ship(CurrentPlayer.PLAYER_TWO, ship_one)
    game_controller.set_player_ship(CurrentPlayer.PLAYER_TWO, ship_two)

    game_controller.construct_players("Felipe", "Henok")

    game_controller.compute_player_guess(Position(5, 5)) == GuessType.DESTROYED

    assert game_controller.current_player_score == 1

    game_controller.alternate_player()

    game_controller.compute_player_guess(Position(6, 5)) == GuessType.HIT

    assert game_controller.current_player_score == 1

def test_get_players_board():
    game_controller = GameController()

    game_controller.construct_players("Felipe", "Henok")

    player_one_board, player_two_board = game_controller.players_board

    assert player_one_board == ShipBoard(10, 10)
    assert player_two_board == ShipBoard(10, 10)
