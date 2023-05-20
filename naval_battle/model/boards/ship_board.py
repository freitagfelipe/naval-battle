from naval_battle.model.boards.board import Board
from naval_battle.model.ship.ship import Ship
from naval_battle.util.enums.cell_type import CellType
from naval_battle.util.min_max_position import min_max_position
from typing import List
from typing import Tuple


class InvalidShip(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ShipBoard(Board):
    def __init__(self, rows: int, columns: int):
        super().__init__(rows, columns)
        self.__ships = []

    @property
    def ships(self) -> List[Ship]:
        return self.__ships

    def set_ship(self, ship: Ship):
        setted, reason = self.__validate_ship(ship)

        if not setted:
            raise InvalidShip(reason)

        min_x, max_x, min_y, max_y = min_max_position(ship.initial_pos, ship.end_pos)

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                self.grid[x][y] = CellType.SHIP

        self.__ships.append(ship)

    def __validate_ship(self, ship: Ship) -> Tuple[bool, str]:
        ship_initial_pos = ship.initial_pos.get()
        ship_end_pos = ship.end_pos.get()

        if not (0 <= ship_initial_pos[0] < self.columns):
            return (False, "A linha da posição inicial está fora do tabuleiro")
        elif not (0 <= ship_end_pos[0] < self.columns):
            return (False, "A linha da posição final está fora do tabuleiro")
        elif not (0 <= ship_initial_pos[1] < self.rows):
            return (False, "A coluna da posição inicial está fora do tabuleiro")
        elif not (0 <= ship_end_pos[1] < self.rows):
            return (False, "A coluna da posição final está fora do tabuleiro")

        min_x = min(ship_initial_pos[0], ship_end_pos[0])
        max_x = max(ship_initial_pos[0], ship_end_pos[0])
        min_y = min(ship_initial_pos[1], ship_end_pos[1])
        max_y = max(ship_initial_pos[1], ship_end_pos[1])

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if self.grid[x][y] == CellType.SHIP:
                    raise InvalidShip("A posição já está ocupada")

        return (True, None)
