from input import take_input
from board import drawn_board
from resolve_win import resolve_win
from check_win import check_win


def game_turn(titles, player):
    take_input(player, titles)
    print(titles)
    return titles


def engine(rows, titles, turn=0):
    win_combinations = resolve_win(rows)
    player_one = 'X'
    player_two = 'O'
    endgame = False
    while endgame is not True:
        if turn % 2 == 0:
            game_turn(titles, player_one)
        else:
            game_turn(titles, player_two)
        turn += 1
        if turn == len(titles):
            return 'tie'
        tmp = check_win(win_combinations, titles)
        if tmp == 'X':
            return 'player_one'
        elif tmp == 'O':
            return 'player_two'
