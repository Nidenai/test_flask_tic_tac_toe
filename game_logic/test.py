from resolve_win import resolve_win


def test_win_combination():
    three_row_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    result = resolve_win(3)
    assert result == three_row_wins

test_win_combination()