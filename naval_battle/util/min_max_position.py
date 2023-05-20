from typing import Tuple
from naval_battle.model.position.position import Position


def min_max_position(
    start_position: Position, end_position: Position
) -> Tuple[int, int, int, int]:
    start_x, start_y = start_position.get()
    end_x, end_y = end_position.get()

    return (
        min(start_x, end_x),
        max(start_x, end_x),
        min(start_y, end_y),
        max(start_y, end_y),
    )
