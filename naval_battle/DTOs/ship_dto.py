from naval_battle.util.enums.ship_type import ShipType
from naval_battle.model.position.position import Position


class ShipDTO:
    def __init__(self, type: ShipType, initial_pos: Position, end_pos: Position):
        self.__type = type
        self.__initial_pos = initial_pos
        self.__end_pos = end_pos

    @property
    def type(self):
        return self.__type

    @property
    def initial_pos(self):
        return self.__initial_pos

    @property
    def end_pos(self):
        return self.__end_pos
