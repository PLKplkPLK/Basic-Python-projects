from multiprocessing.sharedctypes import Value
from random import randint as rand
import re

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
    
    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        num_neighboring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size, row+2)):
            for c in range(min(0,col-1), min(self.dim_size,col+2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r,c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '

        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

        

def play(dim=10, num_bombs=10):
    board = Board(dim, num_bombs)
    print('Input place to check "row,col". Like this: 2,3')
    wyn = True
    while len(board.dug) < board.dim_size **2 - num_bombs:
        print(board)

        try:
            m = re.split(',(\\s)*',input("Check: "))
            m,n = int(m[0]), int(m[-1])
        except ValueError:
            print("Invalid input")
            continue
        if m < 0 or m >= board.dim_size or n < 0 or n >= board.dim_size:
            print("Invalid location.")
            continue

        wyn = board.dig(m,n)

        if not wyn:
            break
    if wyn:
        print("Wygrałeś")
    else:
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
        print("Przegrałeś")



if __name__ == '__main__':
    play()
