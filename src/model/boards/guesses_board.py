from src.model.boards.board import Board
from src.model.boards.ship_board import ShipBoard
from src.model.ship.ship import Ship
from src.model.position.position import Position
from src.util.enums.cell_type import CellType
from src.util.enums.guess_type import GuessType
from src.util.min_max_position import min_max_position
import copy


class GuessesBoardException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class GuessesBoard(Board):
    def __init__(self, ship_board: ShipBoard):
        super().__init__(ship_board.rows, ship_board.columns)
        self.grid = copy.deepcopy(ship_board.grid)
        self.__enemy_ships = ship_board.ships

    def make_guess(self, position: Position) -> GuessType:
        x, y = position.get()

        try:
            self.__validate_position(position)

            if self.grid[x][y] == CellType.SHIP:
                self.grid[x][y] = CellType.HIT

                if self.__was_ship_destroyed(position):
                    return GuessType.DESTROYED

                return GuessType.HIT
            elif self.grid[x][y] == CellType.WATER:
                self.grid[x][y] = CellType.ERROR

                return GuessType.ERROR
        except GuessesBoardException as error:
            raise error

    def __was_ship_destroyed(self, position: Position) -> bool:
        hitted_ship = self.__search_hitted_ship(position)

        min_x, max_x, min_y, max_y = min_max_position(
            hitted_ship.initial_pos, hitted_ship.end_pos
        )

        hitts_qtdd = 0

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if self.grid[x][y] == CellType.HIT:
                    hitts_qtdd += 1

        if hitts_qtdd == hitted_ship.type.value:
            return True
        else:
            return False

    def __search_hitted_ship(self, position: Position) -> Ship:
        hitted_ship = None

        for ship in self.__enemy_ships:
            min_x, max_x, min_y, max_y = min_max_position(
                ship.initial_pos, ship.end_pos
            )

            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if Position(x, y) == position:
                        hitted_ship = ship
                        break
                if hitted_ship != None:
                    break

        return hitted_ship

    def __validate_position(self, position: Position):
        x, y = position.get()

        if not 0 <= x < self.rows:
            raise GuessesBoardException("A linha do palpite está fora do board")
        elif not 0 <= y < self.columns:
            raise GuessesBoardException("A coluna do palpite está fora do board")
        elif self.grid[x][y] == CellType.HIT or self.grid[x][y] == CellType.ERROR:
            raise GuessesBoardException("A posicão já foi escolhida anteriormente")
