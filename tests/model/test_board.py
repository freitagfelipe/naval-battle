from src.model.board import Board, CellType


def test_constructor():
    board = Board(2, 2)

    expected_grid = [[CellType.WATER, CellType.WATER], [CellType.WATER, CellType.WATER]]

    assert board.get_rows() == 2
    assert board.get_columns() == 2
    assert board.get_grid() == expected_grid
