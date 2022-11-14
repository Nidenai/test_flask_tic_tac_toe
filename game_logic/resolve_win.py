from board import drawn_board


def horizontal_elements(rows):
    wins = []
    tiles = drawn_board(rows)
    horizontal_element = 1
    while horizontal_element < len(tiles):
        q = []
        adding = 0
        while adding < rows:
            q.append(horizontal_element + adding)
            adding = adding + 1
        wins.append(q)
        horizontal_element = horizontal_element + rows
    return wins


def vertical_elements(rows):
    wins = []
    vertical_element = 1
    while vertical_element <= rows:
        list = []
        adding = 0
        count = 0
        while count < rows:
            list.append(vertical_element + adding)
            adding = adding + 3
            count = count + 1
        wins.append(list)
        vertical_element = vertical_element + 1
    return wins


def diagonal_elements(rows):
    wins = []
    diagonal_element = 1
    count = 0
    adding = 0
    diagonal = []
    while count < rows:
        diagonal.append(diagonal_element + adding)
        adding += (rows + 1)
        count += 1
    wins.append(diagonal)
    reversal_diagonal_element = rows
    count = 0
    adding = 0
    reverse_diagonal = []
    while count < rows:
        reverse_diagonal.append(reversal_diagonal_element + adding)
        adding += (rows - 1)
        count += 1
    wins.append(reverse_diagonal)
    return wins


def resolve_win(rows):
    hor_el = horizontal_elements(rows)
    ver_el = vertical_elements(rows)
    diagon = diagonal_elements(rows)
    result = hor_el + ver_el + diagon
    return result
