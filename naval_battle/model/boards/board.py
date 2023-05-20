from naval_battle.util.enums.cell_type import CellType
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
    
    def __str__(self) -> str:       
        grid = self.grid
        output = "   0️⃣  1️⃣  2️⃣  3️⃣  4️⃣  5️⃣  6️⃣  7️⃣  8️⃣  9️⃣"
        numbers_emoji = [emoji for emoji in output.split(" ") if emoji != ""]
        
        for i,row in enumerate(grid):
            output += "\n"
            output += numbers_emoji[i] + " "
            
            for column in row:
                if column == CellType.WATER:
                    output += str(" 🟦")
                elif column == CellType.SHIP:
                    output += str(" 🚢")
                elif column == CellType.ERROR:
                    output += str(" 💣")
                elif column == CellType.SHIP:
                    output += str(" 🚢")
            
        return output
