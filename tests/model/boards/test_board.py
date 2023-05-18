from src.model.boards.board import Board, CellType


def test_grid_getter():
    board = Board(2, 2)

    expected_grid = [[CellType.WATER, CellType.WATER], [CellType.WATER, CellType.WATER]]

    assert board.grid == expected_grid


def test_rows_getter():
    board = Board(2, 3)

    assert board.rows == 2


def test_columns_getter():
    board = Board(2, 3)

    assert board.columns == 3
