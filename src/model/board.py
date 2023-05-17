from src.model.cell_type import CellType
from typing import List


class Board:
    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns
        self.__grid = [[CellType.WATER for _ in range(columns)] for _ in range(rows)]

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns

    def get_grid(self) -> list[list[CellType]]:
        return self.__grid
