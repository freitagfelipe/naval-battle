from naval_battle.DTOs.ship_dto import ShipDTO
from naval_battle.model.position.position import Position
from naval_battle.util.enums.ship_type import ShipType


class ShipException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Ship:
    def __init__(self, ship_dto: ShipDTO):
        type = ship_dto.type
        initial_pos = ship_dto.initial_pos
        end_pos = ship_dto.end_pos

        Ship.__check_ship(type, initial_pos, end_pos)
        self.__type = type
        self.__initial_pos = initial_pos
        self.__end_pos = end_pos

    @property
    def initial_pos(self) -> Position:
        return self.__initial_pos

    @property
    def end_pos(self) -> Position:
        return self.__end_pos

    @property
    def type(self) -> ShipType:
        return self.__type

    def __check_ship(type: ShipType, initial_pos: Position, end_pos: Position):
        if type == ShipType.SUBMARINE and initial_pos != end_pos:
            raise ShipException("O submarino deve começar e terminar na mesma posição")

        initial_x, initial_y = initial_pos.get()
        end_x, end_y = end_pos.get()

        if initial_x != end_x and initial_y != end_y:
            raise ShipException("O navio não pode estar na diagonal")

        diff = abs(initial_y - end_y) if initial_x == end_x else abs(initial_x - end_x)

        if type == ShipType.SMALL_SHIP and diff != 1:
            raise ShipException("O navio pequeno deve ter dois de tamanho")
        elif type == ShipType.MEDIUM_SHIP and diff != 2:
            raise ShipException("O navio médio deve ter três de tamanho")
        elif type == ShipType.BIG_SHIP and diff != 3:
            raise ShipException("O navio grande deve ter quatro de tamanho")
