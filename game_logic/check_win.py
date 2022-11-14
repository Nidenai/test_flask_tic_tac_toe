def check_win(win_combinations, titles):
    for combiation in win_combinations:
        check_list = []
        for item in combiation:
            check_list.append(titles[item-1])
        check_first = all([x == 'X' for x in check_list])
        check_second = all([x == 'O' for x in check_list])
        if check_first is True:
            return 'X'
        elif check_second is True:
            return 'O'
    else:
        return False
