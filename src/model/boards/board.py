from src.model.enums.cell_type import CellType
from typing import List


class Board:
    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns
        self.__grid = [[CellType.WATER for _ in range(columns)] for _ in range(rows)]

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    @property
    def grid(self) -> List[List[CellType]]:
        return self.__grid
