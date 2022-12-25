def placing(place, to_put):
    valid_places = ['C', 'L', 'R', 'U', 'D', 'BR', 'BL', 'TR', 'TL']
    if place in valid_places:
        if place == 'C':
            if board[1][1] == ' ':
                board[1][1] = to_put
            else:
                return 'already played'
        elif place == 'R':
            if board[1][2] == ' ':
                board[1][2] = to_put
            else:
                return 'already played'
        elif place == 'L':
            if board[1][0] == ' ':
                board[1][0] = to_put
            else:
                return 'already played'
        elif place == 'U':
            if board[0][1] == ' ':
                board[0][1] = to_put
            else:
                return 'already played'
        elif place == 'D':
            if board[2][1] == ' ':
                board[2][1] = to_put
            else:
                return 'already played'
        elif place == 'TR':
            if board[0][2] == ' ':
                board[0][2] = to_put
            else:
                return 'already played'
        elif place == 'TL':
            if board[0][0] == ' ':
                board[0][0] = to_put
            else:
                return 'already played'
        elif place == 'BR':
            if board[2][2] == ' ':
                board[2][2] = to_put
            else:
                return 'already played'
        elif place == 'BL':
            if board[2][0] == ' ':
                board[2][0] = to_put
            else:
                return 'already played'
    else:
        return 'already played'


def check_win(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' ':
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' ':
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' ':
        return True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ':
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ':
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' ':
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != ' ':
        return True
    else:
        return False


def print_board():
    for i in board:
        print(' | '.join(i))


print('Wellcome to TIC TAC TOE')

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
print_board()

print('How to play:'
      'C = center, L = left, R = right'
      'U = up, D = down, TR = top right'
      'TL = top left, BR = bottom right, BL = bottom left')

while True:
    x_place = input('Where do you want to play X? \n')
    while placing(x_place, 'X') == 'already played':
        x_place = input('Enter a valid X? \n')

    if check_win(board):
        print('Player X won')
        print_board()
        break

    print_board()

    o_place = input('Where do you want to play O? \n')
    while placing(o_place, 'O') == 'already played':
        o_place = input('Enter a valid O? \n')
    if check_win(board):
        print('Player O won')
        print_board()
        break
    print_board()
