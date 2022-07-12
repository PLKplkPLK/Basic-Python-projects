from random import randint as rand

class Board:
    def __init__(self, dim, nb):
        self.dim_size = dim
        self.num_bombs = nb

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()
    
    def make_new_board(self):
        board = [[None for x in range(self.dim_size)] for x in range(self.dim_size)]
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc1 = rand(0,self.dim_size-1)
            loc2 = rand(0,self.dim_size-1)
            if board[loc1][loc2] == '*':
                continue
            board[loc1][loc2] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for i in range(self.dim_size):
            for j in range(self.dim_size):
                if self.board[i][j] == '*':
                    continue
                self.board[i][j] = self.get_num_neighboring_bombs(i,j)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size, row+2)):
            for c in range(min(0,col-1), min(self.dim_size,col+2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs


def play(dim=10, num_bombs=10):
    board = Board(dim, num_bombs)
    string = 'X'
    for i in range(dim):
        string += f' | {i}'
    print(string)
    for i in range(dim):
        string = f'{i}'
        for j in range(dim):
            string += f' |  '
        print(string)
    

if __name__ == '__main__':
    play()