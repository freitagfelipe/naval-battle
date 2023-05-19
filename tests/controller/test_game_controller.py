from src.controller.game_controller import GameController, Player, Position, GuessType
from src.model.boards.ships_board import ShipBoard
from src.model.ship.ship import Ship, ShipType


def test_compute_alternate_player():
    ship_board = ShipBoard(10, 10)

    player_one = Player("Felipe", ship_board)
    player_two = Player("Henok", ship_board)

    game_controller = GameController(player_one, player_two)

    assert game_controller.alternate_player() == "Henok"
    assert game_controller.alternate_player() == "Felipe"


def test_compute_player_guess():
    ship_board = ShipBoard(10, 10)

    ship_board.set_ship(Ship(ShipType.SUBMARINE, Position(5, 5), Position(5, 5)))
    ship_board.set_ship(Ship(ShipType.SMALL_SHIP, Position(6, 5), Position(7, 5)))

    player_one = Player("Felipe", ship_board)
    player_two = Player("Henok", ship_board)

    game_controller = GameController(player_one, player_two)

    assert game_controller.compute_player_guess(Position(5, 5)) == GuessType.DESTROYED

    game_controller.alternate_player()

    assert game_controller.compute_player_guess(Position(6, 5)) == GuessType.HIT

    game_controller.alternate_player()

    assert game_controller.compute_player_guess(Position(3, 3)) == GuessType.ERROR


def test_get_player_score():
    ship_board = ShipBoard(10, 10)

    ship_board.set_ship(Ship(ShipType.SUBMARINE, Position(5, 5), Position(5, 5)))
    ship_board.set_ship(Ship(ShipType.SMALL_SHIP, Position(6, 5), Position(7, 5)))

    player_one = Player("Felipe", ship_board)
    player_two = Player("Henok", ship_board)

    game_controller = GameController(player_one, player_two)

    game_controller.compute_player_guess(Position(5, 5)) == GuessType.DESTROYED

    assert game_controller.current_player_score == 1

    game_controller.alternate_player()

    assert game_controller.compute_player_guess(Position(6, 5)) == GuessType.HIT

    assert game_controller.current_player_score == 1


def test_get_players_board():
    ship_board = ShipBoard(10, 10)

    player_one = Player("Felipe", ship_board)
    player_two = Player("Henok", ship_board)

    game_controller = GameController(player_one, player_two)

    player_one_board, player_two_board = game_controller.players_board

    assert player_one_board == ship_board
    assert player_two_board == ship_board
