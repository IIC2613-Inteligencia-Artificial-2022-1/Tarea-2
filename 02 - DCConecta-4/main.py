import time

from score import two_next_to, three_next_to
from player import HumanPlayer, AiPlayer
from game import Connect4


def main():
    # If you don't want prints, change verbose to False  
    verbose = True
    sleep_time = 0.5
   
    # The human player is always 'X' and the computer is 'O'
    player1 = AiPlayer(token = "X", score_function = two_next_to)
    player2 = AiPlayer(token = "O", score_function = three_next_to)

    # If you want to play against the computer then write the following code: 
    # player1 = HumanPlayer(token = "X")

    # First, we initialize the game 
    match = Connect4()
    # Print board
    if verbose:
        match.print_board()
        print('To play: enter an integer between 1 to 7 ' +
            'corresponding to each column in the board. ' +
            'Whoever stacks 4 pieces next to each other, ' +
            'either horizontally, vertically or diagonally wins.')

    # Turns and game. "game" represents if the game is over or not
    game = False
    while not game:
        # X player (human player)

        # The player chooses his move
        pos, bomb = player1.pick_movement(match)
        print(f"Players 1 Turn {player1.token}")
        print(f"Player 1 played in column {pos} with the use of {bomb[1]} bomb")


        # Use the bomb if one of them is chosen
        if bomb[0]:
            if bomb[1] == "vertical":
                match.vertical_bomb(pos)
                player1.vertical_bomb_available = False

            elif bomb[1] == "horizontal":
                match.horizontal_bomb(pos)
                player1.horizontal_bomb_available = False

            elif bomb[1] == "classic":
                match.classic_bomb(pos)
                player1.classic_bomb_available = False

        # Move
        else:
            match.move(pos, player1.token)

        if verbose:          
            match.print_board()
        # Check if the game is over 
        game = match.check_win(player1.token)       
        if game:
            if verbose:
                print('X wins!')
            winner = 'X'
            break

        time.sleep(sleep_time)

        # O player (computer == minmax)
        # The computer chooses his move
        pos, bomb = player2.pick_movement(match)
        print(f"Players 2 Turn {player2.token}")
        print(f"Player 2 played in column {pos} with the use of {bomb[1]} bomb")


        # Use the bombs
        if bomb[0]:
            if bomb[1] == "vertical":
                match.vertical_bomb(pos)
                player2.vertical_bomb_available = False

            elif bomb[1] == "horizontal":
                match.horizontal_bomb(pos)
                player2.horizontal_bomb_available = False

            elif bomb[1] == "classic":
                match.classic_bomb(pos)
                player2.classic_bomb_available = False

        # Move
        else:
            match.move(pos, player2.token)          
        if verbose:
            match.print_board()

        # Check if the game is over
        game = match.check_win(player2.token)       
        if game:
            if verbose:
                print('O wins!')
            winner = 'O'

    if verbose:
        print('Good game.')
    return winner

if __name__ == '__main__':
    main()
