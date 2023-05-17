from typing import Tuple


class Position:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get(self) -> Tuple[int, int]:
        return (self.__x, self.__y)
