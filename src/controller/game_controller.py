from src.model.player.player import Player
from src.model.position.position import Position
from src.model.enums.current_player import CurrentPlayer
from src.model.boards.guesses_board import GuessesBoard, GuessType
from typing import Tuple


class GameController:
    def __init__(self, player_one: Player, player_two: Player):
        self.__current_player = CurrentPlayer.PLAYER_ONE
        self.__player_one = player_one
        self.__player_two = player_two

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
