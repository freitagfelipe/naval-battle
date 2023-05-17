from src.model.position import Position
from src.model.ship_type import ShipType


class Ship:
    def __init__(self, type: ShipType, initial_pos: Position, end_pos: Position):
        self.__type = type
        self.__initial_pos = initial_pos
        self.__end_pos = end_pos

    def get_initial_pos(self) -> Position:
        return self.__initial_pos

    def get_end_pos(self) -> Position:
        return self.__end_pos

    def get_type(self) -> ShipType:
        return self.__type
