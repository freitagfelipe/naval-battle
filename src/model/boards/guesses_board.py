from src.model.boards.board import Board
from src.model.boards.ships_board import ShipBoard
from src.model.position.position import Position
from src.model.enums.cell_type import CellType
import copy


class GuessesBoardException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class GuessesBoard(Board):
    def __init__(self, ships_board: ShipBoard):
        super().__init__(ships_board.rows, ships_board.columns)
        self.grid = copy.deepcopy(ships_board.grid)

    def make_guess(self, position: Position) -> bool:
        x, y = position.get()

        try:
            self.__validate_position(position)

            if self.grid[x][y] == CellType.SHIP:
                self.grid[x][y] = CellType.HIT
                return True
            elif self.grid[x][y] == CellType.WATER:
                self.grid[x][y] = CellType.ERROR
                return False
        except GuessesBoardException as error:
            raise error

    def __validate_position(self, position: Position):
        x, y = position.get()

        if not 0 <= x < self.rows:
            raise GuessesBoardException("A linha do palpite está fora do board")
        elif not 0 <= y < self.columns:
            raise GuessesBoardException("A coluna do palpite está fora do board")
        elif self.grid[x][y] == CellType.HIT or self.grid[x][y] == CellType.ERROR:
            raise GuessesBoardException("A posicão já foi escolhida anteriormente")
