from rubik.cube import Cube
import random

class RCube(Cube):
    sol = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
    moves = {
         Cube.L:Cube.Li,
         Cube.Li:Cube.L,
         Cube.R:Cube.Ri,
         Cube.Ri:Cube.R,
         Cube.U:Cube.Ui,
         Cube.Ui:Cube.U,
         Cube.D:Cube.Di,
         Cube.Di:Cube.D,
         Cube.F:Cube.Fi,
         Cube.Fi:Cube.F,
         Cube.B:Cube.Bi,
         Cube.Bi:Cube.B}
    
    def __init__(self,state, shuffle = False, verbose = 0, complexity = 1):
        super().__init__(state)
        self.shuffle = shuffle
        if self.shuffle:
            self.shuffle_cube(complexity, verbose)
        self.last_move = None
    
    def random_move(self):
        random.choice(list(self.moves.keys()))(self)

    def shuffle_cube(self, complexity, verbose):
        if verbose != 0:
                print(self)
                print('\n----------------------\n')

        for _ in range(complexity):
            self.random_move()
            if verbose == 2:
                print(self)
                print('\n----------------------\n')

        if verbose == 1:
            print(self)
            print('\n----------------------\n')

    def reverse_last_move(self):
        if self.last_move:
            self.moves[self.last_move](self)

    def succesors(self):
        for move, inverse in RCube.moves.items():
            move(self)
            state = self.flat_str()
            inverse(self)
            move_str = str(move).split('.')[-1].split(' ')[0]
            yield state, move_str, 1
        