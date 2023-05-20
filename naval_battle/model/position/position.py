from typing import Tuple
from typing import TypeVar

Self = TypeVar("Self", bound="Position")


class Position:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get(self) -> Tuple[int, int]:
        return (self.__x, self.__y)

    def __eq__(self, other: Self) -> bool:
        return self.__x == other.__x and self.__y == other.__y

    def __str__(self) -> str:
        return f"{self.__y},{self.__x}"
