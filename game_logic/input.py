from board import drawn_board


def take_input(player_token, titles):
    while True:
        value = input('Where to put: ' + player_token + ' ?  ')
        try:
            value = int(value)
        except:
            print('Error typping')
            continue
        value = int(value)
        if value >= 1 and value <= len(titles):
            if str(titles[value - 1]) in 'XO':
                print('This tile already used')
                continue
        else:
            print('Not correct number')
            continue
        titles[value - 1] = player_token
        break
