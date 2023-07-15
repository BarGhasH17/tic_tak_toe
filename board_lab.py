class BoardLab:

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def placing(self, place, to_put):
        valid_places = ['C', 'L', 'R', 'U', 'D', 'BR', 'BL', 'TR', 'TL']
        if place in valid_places:
            if place == 'C':
                if self.board[1][1] == ' ':
                    self.board[1][1] = to_put
                else:
                    return 'already played'
            elif place == 'R':
                if self.board[1][2] == ' ':
                    self.board[1][2] = to_put
                else:
                    return 'already played'
            elif place == 'L':
                if self.board[1][0] == ' ':
                    self.board[1][0] = to_put
                else:
                    return 'already played'
            elif place == 'U':
                if self.board[0][1] == ' ':
                    self.board[0][1] = to_put
                else:
                    return 'already played'
            elif place == 'D':
                if self.board[2][1] == ' ':
                    self.board[2][1] = to_put
                else:
                    return 'already played'
            elif place == 'TR':
                if self.board[0][2] == ' ':
                    self.board[0][2] = to_put
                else:
                    return 'already played'
            elif place == 'TL':
                if self.board[0][0] == ' ':
                    self.board[0][0] = to_put
                else:
                    return 'already played'
            elif place == 'BR':
                if self.board[2][2] == ' ':
                    self.board[2][2] = to_put
                else:
                    return 'already played'
            elif place == 'BL':
                if self.board[2][0] == ' ':
                    self.board[2][0] = to_put
                else:
                    return 'already played'
        else:
            return 'already played'

    def check_win(self, board):
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

    def print_board(self):
        for i in self.board:
            print(' | '.join(i))