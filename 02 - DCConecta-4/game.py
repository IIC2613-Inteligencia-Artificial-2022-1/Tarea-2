# Código extraido de
# https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf


# Class stack (for each column)
class Stack:
        def __init__(self):
            self._list = []
            self.stack_index = 5

        def __len__(self):
            return len(self._list)

        def push(self, element):
            if len(self._list) <= 6:
                self._list.append(element)
            else:
                return
        
        def peek(self):
            return self._list[-1]


class Connect4:
    def __init__(self):
        self.columns = 7
        self.rows = ['a', 'b', 'c', 'd', 'e', 'f']
        self.set_columns = {1, 2, 3, 4, 5, 6, 7}
        self.board = self.init_board()
        self.stacks = self.init_stacks()


    # Initialize board (empty)
    def init_board(self):
        # empty board
        board = []
        for i in range(0, len(self.rows)):
            board.append([' '] * 7)
        return board

    # Initialize stacks (empty)
    def init_stacks(self):
        # empty stack
        stacks = []
        for i in range(self.columns):
            column = Stack()
            stacks.append(column)
        return stacks

    # print board
    def print_board(self):
        rows = ['a', 'b', 'c', 'd', 'e', 'f']
        top = '    1   2   3   4   5   6   7   '
        row = [[n] for n in range(0, 7)]
        row[0][0] = 'f | '
        row[1][0] = 'e | '
        row[2][0] = 'd | '
        row[3][0] = 'c | '
        row[4][0] = 'b | '
        row[5][0] = 'a | '
        print('')
        print('  ' + '-' * (len(top) - 3))
        for j in range(0, len(rows)):
            for i in range(1, 8):
                row[j][0] = row[j][0] + str(self.board[j][i - 1]) + ' | '
            print(row[j][0])
            print('  ' + '-' * ((len(row[j][0]) - 3)))
        print(top)
        print('')

    # Given the pos and token, makes the move on the board
    def move(self, pos, token):
        self.stacks[pos - 1].push(token)
        self.board[6 - len(self.stacks[pos - 1])][pos - 1] = self.stacks[pos - 1].peek()
    
    # Check wins
    def check_win(self, token):  # S is a string X O
        game = False
        # Horizontal checker
        for j in range(0, 6):
            for i in range(3, 7):
                if (self.board[j][i] == self.board[j][i - 1] ==
                        self.board[j][i - 2] == self.board[j][i - 3] == token):
                    game = True

        # Vertical checker
        for i in range(0, 7):
            for j in range(3, 6):
                if (self.board[j][i] == self.board[j - 1][i] ==
                        self.board[j - 2][i] == self.board[j - 3][i] == token):
                    game = True

        # Diagonal checker
        for i in range(0, 4):
            for j in range(0, 3):
                if (self.board[j][i] == self.board[j + 1][i + 1] ==
                    self.board[j + 2][i + 2] == self.board[j + 3][i + 3] == token or
                    self.board[j + 3][i] == self.board[j + 2][i + 1] ==
                        self.board[j + 1][i + 2] == self.board[j][i + 3] == token):
                    game = True
        return game

    
    # BOMBS 
    # Vertical
    def vertical_bomb(self, pos):
        del self.stacks[pos - 1]._list[:]                   # This cleans the stack

        for i in range(len(self.board)):                    # This cleans the board
            self.board[i][pos - 1] = " "             

    # Horizontal
    def horizontal_bomb(self, pos):                         
        index = len(self.stacks[pos - 1])                   # This actualize the stack
        if index > 0:
            index = index - 1
        for i in range(len(self.stacks)):
            if (len(self.stacks[i]._list) - 1) >= index:
                self.stacks[i]._list.pop(index)

        new_board = self.init_board()                       # This actualize the board
        for i in range(len(self.stacks)):
            for j in range(len(self.stacks[i])):
                index = 5 - j
                new_board[index][i] = self.stacks[i]._list[j]
        self.board = new_board

    # Classic bomb, applies both vertical and horizontal bombs 
    def classic_bomb(self, pos):
        self.horizontal_bomb(pos)
        self.vertical_bomb(pos)
