from itertools import groupby


def get_turn_sequence(data):
    """Функция берет данные из словаря json и переводит их в список"""
    turn_sequence = []
    for key, value in data.items():
        coordinates = []
        for type_coordinate, coordinate in value.items():
            coordinates.append(coordinate)
        turn_sequence.append(coordinates)
    return turn_sequence


def game_turn(player_turn_sequence, coordinate_x, coodrinate_y):
    """Функция принимает на ввод новую точку и добавляет ее в список точек пользователя"""
    player_turn_sequence.append([coordinate_x, coodrinate_y])
    return player_turn_sequence


def check_empty_tile(player_one_sequence, player_two_sequence, coordinate_x, coordinate_y):
    """Функция проверяет, не занята ли уже точка кем-то другим"""
    for item in player_one_sequence:
        if item[0] == coordinate_x and item[1] == coordinate_y:
            return False
    for item in player_two_sequence:
        if item[0] == coordinate_x and item[1] == coordinate_y:
            return False
    return True


def return_game_data(turn_sequence):
    """Функция принимает данные в виде списка и возвращает их обратно в виде словаря"""
    data = {}
    turn = 1
    while turn <= len(turn_sequence):
        data[turn] = {
            'coordinate x': turn_sequence[turn - 1][0],
            'coordinate y': turn_sequence[turn - 1][1]
        }
        turn += 1
    return data


def check_win_straight(turn_sequence, rows, axis):
    """Функция проверяет победную последовательность по вертикали и горизонтали и возвращает True,
    если последовательность найдена """
    coordinates = []

    for item in turn_sequence:
        coordinates.append(item[axis])
    coordinates.sort()

    coordinates = [el for el, _ in groupby(coordinates)]

    for item in coordinates:
        win_sequence = []
        count = 0
        while count < rows:
            win_sequence.append(item + count)
            if count > 0:
                win_sequence.insert(0, item - count)
            count += 1
        start_list = 0
        end_list = start_list + rows
        while end_list <= len(coordinates):
            probably_win_combination = coordinates[start_list:end_list]
            start_list += 1
            end_list += 1
            start_cheking_list = 0
            end_checking_list = start_cheking_list + len(probably_win_combination)
            while end_checking_list <= len(win_sequence):
                compate_combination = win_sequence[start_cheking_list:end_checking_list]
                start_cheking_list += 1
                end_checking_list += 1
                if compate_combination == probably_win_combination:
                    return True

    return False


def check_win_diaoganies(turn_sequence, number_of_titles):
    """"Функция проверяет победную последовательность по диагонали в обеих направлениях"""
    turn_sequence.sort()
    # print(f'this is turn sequence {turn_sequence}')
    for element in turn_sequence:
        win_sequence = []
        win_sequence_reverse = []
        count = 0
        while count < number_of_titles:
            win_sequence.append([element[0] + count, element[1] + count])
            win_sequence_reverse.append([element[0] - count, element[1] + count])
            if count > 0:
                win_sequence.insert(0, [element[0] - count, element[1] - count])
                win_sequence_reverse.insert(0, [element[0] + count, element[1] - count])
            count += 1
        # print(f'this is win_sequence for element {element}:  {win_sequence}')
        # print(f'this is win_sequence for element {element}:  {win_sequence_reverse}')
        start_list = 0
        end_list = start_list + number_of_titles
        while end_list <= len(turn_sequence):
            probably_win_combination = turn_sequence[start_list:end_list]
            # print(f'this is probably win combination {probably_win_combination}')
            start_list += 1
            end_list += 1
            start_cheking_list = 0
            end_checking_list = start_cheking_list + len(probably_win_combination)
            while end_checking_list <= len(win_sequence):
                compate_combination = win_sequence[start_cheking_list:end_checking_list]
                # print(compate_combination)
                compare_reverse_combination = win_sequence_reverse[start_cheking_list:end_checking_list]
                # print(compare_reverse_combination)
                start_cheking_list += 1
                end_checking_list += 1
                # print(f'comparing {compate_combination} and {probably_win_combination}')
                # print(f'comparing {compare_reverse_combination} and {probably_win_combination}')
                if compate_combination == probably_win_combination:

                    return True
                elif compare_reverse_combination == probably_win_combination:

                    return True
        # print('end')
    return False


def game_round(player_one_sequence, player_two_sequence):
    """Общий игровой раунд"""
    end_player_two_turn = False
    while end_player_two_turn is False:
        coordinate_x = int(input(f'Player two press X coordinate: '))
        coordinate_y = int(input(f'Player two press Y coordinate: '))

        check_tile = check_empty_tile(player_one_sequence, player_two_sequence, int(coordinate_x), int(coordinate_y))
        if check_tile == False:
            print('This tile already not empty')
            continue
        else:
            player_two_sequence = game_turn(player_two_sequence, int(coordinate_x), int(coordinate_y))
            end_player_two_turn = True
    end_player_one_turn = False
    while end_player_one_turn is False:
        coordinate_x = input(f'Player one press X coordinate: ')
        coordinate_y = input(f'Player one press Y coordinate: ')
        check_tile = check_empty_tile(player_one_sequence, player_two_sequence, int(coordinate_x), int(coordinate_y))
        if check_tile == False:
            print('This tile already not empty')
            continue
        else:
            player_one_sequence = game_turn(player_one_sequence, int(coordinate_x), int(coordinate_y))
            end_player_one_turn = True
    return (player_one_sequence, player_two_sequence)


def game(number_titles_for_win):
    turn = 0
    win = False
    player_win = None
    player_one_turn_sequence = [[0, 0]]
    player_two_turn_sequence = []
    while win is not True:
        round_result = game_round(player_one_turn_sequence, player_two_turn_sequence)
        player_one, player_two = round_result
        turn += 1
        if turn >= number_titles_for_win - 1:

            x_sequence_check = check_win_straight(player_one, number_titles_for_win, 0)
            y_sequence_check = check_win_straight(player_one, number_titles_for_win, 1)
            diagon_sequence = check_win_diaoganies(player_one, number_titles_for_win)

            if x_sequence_check == True or y_sequence_check == True or diagon_sequence == True:
                player_win = 1
                win = True
                break
            x_sequence_check = check_win_straight(player_two, number_titles_for_win, 0)
            y_sequence_check = check_win_straight(player_two, number_titles_for_win, 1)
            diagon_sequence = check_win_diaoganies(player_two, number_titles_for_win)

            if x_sequence_check == True or y_sequence_check == True or diagon_sequence == True:
                player_win = 2
                win = True
                break

    if player_win == 1:
        print('one win')
    elif player_win == 2:
        print('two win')


game(3)