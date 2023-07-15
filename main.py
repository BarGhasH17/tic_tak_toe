import board_lab

print('Wellcome to TIC TAC TOE')

bl = board_lab.BoardLab()
bl.print_board()

print('How to play:'
      'C = center, L = left, R = right'
      'U = up, D = down, TR = top right'
      'TL = top left, BR = bottom right, BL = bottom left')

while True:
    x_place = input('Where do you want to play X? \n')
    while bl.placing(x_place, 'X') == 'already played':
        x_place = input('Enter a valid X? \n')

    if bl.check_win(bl.board):
        print('Player X won')
        bl.print_board()
        break

    bl.print_board()

    o_place = input('Where do you want to play O? \n')
    while bl.placing(o_place, 'O') == 'already played':
        o_place = input('Enter a valid O? \n')
    if bl.check_win(bl.board):
        print('Player O won')
        bl.print_board()
        break
    bl.print_board()
