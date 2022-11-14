def drawn_board(rows):
    tiles = []
    for number in range(rows * rows):
        tiles.append(number + 1)
    return tiles
