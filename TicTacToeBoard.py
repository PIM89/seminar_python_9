class TicTacToeBoard:
    def __init__(self):
        self.list_elem = [['-' for _ in range(3)] for _ in range(3)]
        self.count = 9
        self.win_coord = (((0, 0), (1, 0), (2,0)), ((1, 0), (1, 1), (1,2)), ((2, 0), (2, 1), (2,2)), ((0, 0), (1, 0), (2,0)),
        ((0, 1), (1, 1), (2,2)), ((0, 2), (1, 2), (2,2)), ((0, 0), (1, 1), (2,2)), ((0, 2), (1, 1), (2,0)))
        self.flag = False

    def new_game(self):
        self.list_elem = [['-' for _ in range(3)] for _ in range(3)]
        self.count = 9
        self.flag = False
        return 'Новая игра создана!'

    def get_field(self):
        return self.list_elem
    
    def check_fiels(self, cross):
        for res in self.win_coord:
            if self.list_elem[res[0][0]][res[0][1]] == self.list_elem[res[1][0]][res[1][1]] == self.list_elem[res[2][0]][res[2][1]]:
                self.flag = True
                return f'Победил игрок {cross}'
            if self.count == 0: return 'Ничья'
            else: return 'Продолжаем играть!'

    def make_move(self, row, col):
        if (self.count % 2): cross = 'X'
        else: cross = 'O'
        if self.list_elem[row-1][col-1] == 'X' or self.list_elem[row-1][col-1] == 'O':
            if self.flag or self.count == 0: return 'Игра уже завершена!'
            else: return f'Клетка {row}, {col} уже занята!'
        else:
            self.list_elem[row-1][col-1] = cross
            self.count -= 1
            return TicTacToeBoard.check_fiels(self, cross)
            

board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")

print('\n')
board_2 = TicTacToeBoard()
print(*board.get_field(), sep="\n")