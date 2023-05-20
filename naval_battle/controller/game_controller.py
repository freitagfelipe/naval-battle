from naval_battle.model.player.player import Player
from naval_battle.model.position.position import Position
from naval_battle.util.enums.current_player import CurrentPlayer
from naval_battle.model.boards.ship_board import ShipBoard, Ship
from naval_battle.model.boards.guesses_board import GuessesBoard, GuessType
from naval_battle.DTOs.ship_dto import ShipDTO
from typing import Tuple


class GameController:
    def __init__(self):
        self.__current_player = CurrentPlayer.PLAYER_ONE
        self.__player_one_ship_board = ShipBoard(10, 10)
        self.__player_two_ship_board = ShipBoard(10, 10)

    def set_player_ship(self, player: CurrentPlayer, ship_dto: ShipDTO):
        ship = Ship(ship_dto)

        if player == CurrentPlayer.PLAYER_ONE:
            self.__player_one_ship_board.set_ship(ship)

            return

        self.__player_two_ship_board.set_ship(ship)

    def construct_players(self, player_one_name: str, player_two_name: str):
        self.__player_one = Player(
            player_one_name, GuessesBoard(self.__player_two_ship_board)
        )
        self.__player_two = Player(
            player_two_name, GuessesBoard(self.__player_one_ship_board)
        )

    def compute_player_guess(self, position: Position) -> GuessType:
        if self.__current_player == CurrentPlayer.PLAYER_ONE:
            return self.__player_one.make_guess(position)

        return self.__player_two.make_guess(position)

    def alternate_player(self) -> str:
        if self.__current_player == CurrentPlayer.PLAYER_ONE:
            self.__current_player = CurrentPlayer.PLAYER_TWO

            return self.__player_two.name

        self.__current_player = CurrentPlayer.PLAYER_ONE

        return self.__player_one.name

    @property
    def current_player_score(self) -> int:
        if self.__current_player == CurrentPlayer.PLAYER_ONE:
            return self.__player_one.score

        return self.__player_two.score

    @property
    def players_board(self) -> Tuple[GuessesBoard, GuessesBoard]:
        return (self.__player_one.guesses_board, self.__player_two.guesses_board)

    def get_player_ship_board(self, player: CurrentPlayer) -> ShipBoard:
        if player == CurrentPlayer.PLAYER_ONE:
            return self.__player_one_ship_board

        return self.__player_two_ship_board
