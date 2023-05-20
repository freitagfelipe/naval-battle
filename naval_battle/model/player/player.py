from naval_battle.model.boards.guesses_board import GuessesBoard, GuessesBoardException
from naval_battle.model.position.position import Position
from naval_battle.util.enums.guess_type import GuessType


class Player:
    def __init__(self, name: str, guesses_board: GuessesBoard):
        self.__name = name
        self.__guesses_board = guesses_board
        self.__score = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def score(self) -> int:
        return self.__score

    @property
    def guesses_board(self) -> GuessesBoard:
        return self.__guesses_board

    def make_guess(self, position: Position) -> GuessType:
        try:
            guess_status = self.guesses_board.make_guess(position)

            if not guess_status == GuessType.ERROR:
                self.__score += 1

            return guess_status
        except GuessesBoardException as error:
            raise error
