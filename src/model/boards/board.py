from src.util.enums.cell_type import CellType
from typing import List
from typing import TypeVar

Self = TypeVar("Self", bound="Board")


class BoardException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Board:
    def __init__(self, rows: int, columns: int):
        if rows <= 0:
            raise BoardException(
                "O board não pode ser criado com um número negativo de linhas"
            )
        elif columns <= 0:
            raise BoardException(
                "O board não pode ser criado com um número negativo de colunas"
            )
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

    @grid.setter
    def grid(self, grid: List[List[CellType]]):
        self.__grid = grid

    def __eq__(self, other: Self) -> bool:
        return self.grid == other.grid
