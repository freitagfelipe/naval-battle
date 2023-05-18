from src.model.board import Board
from src.model.ship import Ship
from src.model.cell_type import CellType
from typing import Tuple


class InvalidShip(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ShipBoard(Board):
    def __init__(self, rows: int, columns: int):
        super().__init__(rows, columns)

    def set_ship(self, ship: Ship):
        setted, reason = self.__validate_ship(ship)
        
        if not setted:
            raise InvalidShip(reason)

        ship_initial_pos = ship.initial_pos.get()
        ship_end_pos = ship.end_pos.get()

        min_x = min(ship_initial_pos[0], ship_end_pos[0])
        max_x = max(ship_initial_pos[0], ship_end_pos[0])
        min_y = min(ship_initial_pos[1], ship_end_pos[1])
        max_y = max(ship_initial_pos[1], ship_end_pos[1])

        print(f"Min_x: {min_x}, Max_x: {max_x}")
        print(f"Min_y: {min_y}, Max_y: {max_y}")

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                print(f"{x} {y}")
                self.grid[x][y] = CellType.SHIP


    def __validate_ship(self, ship: Ship) -> Tuple[bool, str]:
        ship_initial_pos = ship.initial_pos.get()
        ship_end_pos = ship.end_pos.get()

        if not 0 <= ship_initial_pos[0] < self.columns:
            return (False, "O x da posição inicial está fora do tabuleiro")
        elif not 0 <= ship_end_pos[0] < self.columns:
            return (False, "O x da posição final está fora do tabuleiro")
        elif not 0 <= ship_initial_pos[1] < self.rows:
            return (False, "O y da posição inicial está fora do tabuleiro")
        elif not 0 <= ship_end_pos[1] < self.rows:
            return (False, "O y da posição final está fora do tabuleiro")

        min_x = min(ship_initial_pos[0], ship_end_pos[0])
        max_x = max(ship_initial_pos[0], ship_end_pos[0])
        min_y = min(ship_initial_pos[1], ship_end_pos[1])
        max_y = max(ship_initial_pos[1], ship_end_pos[1])

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if self.grid[x][y] == CellType.SHIP:
                    raise InvalidShip("A posição já está ocupada")
                
        return (True, None)
