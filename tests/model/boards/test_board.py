from naval_battle.model.boards.board import Board, CellType, BoardException
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
    with pytest.raises(
        BoardException,
        match="O board não pode ser criado com um número negativo de linhas",
    ):
        Board(-1, 2)


def test_create_board_with_negative_column_should_fail():
    with pytest.raises(
        BoardException,
        match="O board não pode ser criado com um número negativo de colunas",
    ):
        Board(2, -1)


def test_create_board_with_more_than_ten_rows_should_fail():
    with pytest.raises(
        BoardException,
        match="O board não pode ser criado com um número maior que dez de linhas",
    ):
        Board(11, 5)


def test_create_board_with_more_than_ten_columns_should_fail():
    with pytest.raises(
        BoardException,
        match="O board não pode ser criado com um número maior que dez de colunas",
    ):
        Board(5, 11)


def test_str_method():
    board = Board(1, 5)

    grid = board.grid

    grid[0][0] = CellType.SHIP

    line_one, line_two = str(board).split("\n")

    assert line_one == "   0️⃣  1️⃣  2️⃣  3️⃣  4️⃣"
    assert line_two == "0️⃣  🚢 🟦 🟦 🟦 🟦"
