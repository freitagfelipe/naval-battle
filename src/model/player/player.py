from src.model.boards.ships_board import ShipBoard
from src.model.boards.guesses_board import GuessesBoard, GuessesBoardException
from src.model.position.position import Position
from src.model.enums.guess_type import GuessType

class Player:
    def __init__(self, name: str, ships_board: ShipBoard, guesses_board: ShipBoard):
        self.__name = name
        self.__ships_board = ships_board
        self.__guesses_board = GuessesBoard(guesses_board)
        self.__score = 0
        self.__round_score = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def score(self) -> int:
        return self.__score

    @property
    def round_score(self) -> int:
        return self.__round_score
    
    @property
    def ships_board(self) -> ShipBoard:
        return self.__ships_board

    @property
    def guesses_board(self) -> GuessesBoard:
        return self.__guesses_board
    
    def set_round_score(self):
        self.__round_score += 1

    def make_guess(self, position: Position) -> GuessType:
        try:
            guess_status = self.guesses_board.make_guess(position)
            
            if not guess_status == GuessType.ERROR:
                self.__score += 1
                
            return guess_status
        except GuessesBoardException as error:
            raise error
