from minimax import minimax
import math


class HumanPlayer:
    def __init__(self, token):
        self.token = token
        # Start on True, when used change to False
        self.horizontal_bomb_available = True
        self.vertical_bomb_available = True
        self.classic_bomb_available = True
        self.bombs = [self.horizontal_bomb_available, self.vertical_bomb_available, 
            self.classic_bomb_available]            # self.bombs = [horizontal, vertical, classic]

    def pick_movement(self, match):
        """
        Returns a tuple (pos, bomb):
 
        pos = position to make the move or throw a bomb (int)
        bomb = [True if bomb movement is selected (False if not), Type of bomb]

        """
        move_done = False
        while move_done == False:
            valid_input_move = False
            while valid_input_move == False:
                pos = input('Where you wanna move/bomb? (pick a column): ')

                if not pos.isnumeric():
                    print("Your input is not valid, try again")
                
                elif pos.isnumeric():
                    pos = int(pos)
                    if pos not in match.set_columns:
                        print("Your input is not valid, try again")
                    else:
                        valid_input_move = True
            
            valid_input_bomb = False
            while valid_input_bomb == False:

                if (self.classic_bomb_available or self.horizontal_bomb_available or
                self.vertical_bomb_available):
                    bomb = input('Do you want to place a bomb? (yes/no): ').lower()

                    if (bomb != "yes") and (bomb != "no"):
                        print("Your input is not valid, try again")
                    else:
                        valid_input_bomb = True
                else:
                    print("You already used all your bombs")
                    bomb = "no"
                    valid_input_bomb = True
            
            if bomb == 'yes':
                valid_input_bomb_select = False
                while valid_input_bomb_select == False:
                    type_bomb = input('Select bomb: (vertical / horizontal / classic): ').lower()

                    if (type_bomb != "vertical" and type_bomb != "horizontal" 
                        and type_bomb != "classic"):
                        print("Your input is not valid, try again")

                    elif type_bomb == 'vertical':
                        if self.vertical_bomb_available:                        
                            valid_input_bomb_select = True
                        else:
                            print("You already used that bomb, try again")

                    elif type_bomb == 'horizontal':
                        if self.horizontal_bomb_available:                        
                            valid_input_bomb_select = True
                        else:
                            print("You already used that bomb, try again")
                    
                    elif type_bomb == 'classic':
                        if self.classic_bomb_available:                        
                            valid_input_bomb_select = True
                        else:
                            print("You already used that bomb, try again")

                if type_bomb == 'vertical':
                    bomb = [True, 'vertical'] 
                    move_done = True

                elif type_bomb == 'horizontal':
                    bomb = [True, 'horizontal']
                    move_done = True
                
                elif type_bomb == 'classic':
                    bomb = [True, 'classic']
                    move_done = True

            else:   #bomb == no ==> move
                if len(match.stacks[pos - 1]) >= 6:
                    print('Column full, try another one...')
                else:
                    bomb = [False, None]
                    move_done = True
        return (pos, bomb)


class AiPlayer:
    def __init__(self, token, score_function):
        self.token = token
        # Start on True, when used change to False
        self.horizontal_bomb_available = True
        self.vertical_bomb_available = True
        self.classic_bomb_available = True
        self.bombs = [self.horizontal_bomb_available, self.vertical_bomb_available, 
            self.classic_bomb_available]            # self.bombs = [horizontal, vertical, classic]

        self.score_function = score_function

    def pick_movement(self, match):
        """
        Returns a tuple (pos, bomb):
 
        pos = position to make the move or throw a bomb (int)
        bomb = [True if bomb movement is selected (False if not), Type of bomb]

        """
        # If the player is the AI         
        column, bomb, _ = minimax(match = match, depth = 5, alpha = -math.inf,
            beta = math.inf, bombs = self.bombs, score_function = self.score_function, 
            maximizing_player=True)
        # We don not use value here, so its replaced with _

        return (column, bomb)
