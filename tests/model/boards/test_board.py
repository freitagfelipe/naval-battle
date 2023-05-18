from src.model.boards.board import Board, CellType, BoardException
import pytest


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

def test_create_board_with_negative_row_should_fail():
    with pytest.raises(BoardException, match="O board não pode ser criado com um número negativo de linhas"):
        Board(-1,2)

def test_create_board_with_negative_column_should_fail():
    with pytest.raises(BoardException, match="O board não pode ser criado com um número negativo de colunas"):
        Board(2,-1)