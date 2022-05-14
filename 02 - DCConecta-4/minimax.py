import math
import random
from copy import deepcopy


def get_valid_locations(stacks, bombs):
  """
  Returns a list of the valid locations to play of the given stacks
  bombs = [horizontal, vertical, classic] (bool)
  """
  valid_locations = [] 
  for i in range(len(stacks)):
    if len(stacks[i]._list) < 6:
      valid_locations.append((i+1, [False, None]))
      if bombs[0]:
        valid_locations.append((i+1, [True, "horizontal"]))
      if bombs[1]:
        valid_locations.append((i+1, [True, "vertical"]))
      if bombs[2]:
        valid_locations.append((i+1, [True, "classic"]))
  return valid_locations


def is_terminal_node(match, bombs):
  """
  Check if the game is over given a board and stacks. Returns True or False
  There are two options that returns 'True':
  1) 'X' or 'O' won 
  2) There are no more valid locations to play.
  """
  return (match.check_win('X') or match.check_win('O') or 
    len(get_valid_locations(match.stacks, bombs)) == 0)


def minimax(match, depth, alpha, beta, bombs, score_function, maximizing_player):
  """
  Minimax algorithm. Given the current match, alpha, beta,
  bombs (= [horizontal, vertical, classic]) and score function 
  returns (column, bomb, value):

  1) column = where to play 
  2) bomb = [True if bomb movement is selected (False if not), Type of bomb]
  3) value = score
  """

  # First we check if we are in the terminal node (or the game is over at the current depth)
  is_terminal = is_terminal_node(match, bombs)
  if depth == 0 or is_terminal:
    if is_terminal:
      if match.check_win("O"):						# Computer won
        return (None, [False, None], math.inf)

      elif match.check_win("X"):						# "Player" won
        return (None, [False, None], -math.inf)

      else: 											# Game is over, no more valid moves
        return (None, [False, None], 0)

    else: 												# Depth is zero	
      if maximizing_player:		
        return (None, [False, None], score_function(match.board, "O"))
      else:
        return (None, [False, None], -score_function(match.board, "X"))

  
  
  if maximizing_player:									# Computer turn at the current depth
    valid_locations = get_valid_locations(match.stacks, bombs)
    value = -math.inf									
    column, bomb = random.choice(valid_locations)		# Random move if there is no better one

    # We expand the nodes for each valid column
    for movement in valid_locations:
      match_copy = deepcopy(match)

      # Bombs
      if movement[1][0]:								
        if movement[1][1] == "horizontal":			# Horizontal bomb
          match_copy.horizontal_bomb(movement[0])
          bombs[0] = False

        elif movement[1][1] == "vertical":			# Vertical bomb
          match_copy.vertical_bomb(movement[0])	
          bombs[1] = False

        elif movement[1][1] == "classic":			# Classic bomb
          match_copy.classic_bomb(movement[0])
          bombs[2] = False

      else:
        # Move at the current column
        match_copy.move(movement[0], "O")

      # Score for the current move 
      new_score = minimax(match_copy, depth-1, alpha, beta, bombs, score_function, False)[2]

      # We check if its the current best move	
      if new_score > value:
        value = new_score
        column = movement[0]
        bomb = movement[1]

    return column, bomb, value

  else:													# "Player" turn at the current depth 
    valid_locations = get_valid_locations(match.stacks, bombs)
    value = math.inf
    column, bomb = random.choice(valid_locations)				# Random move if there is no better one
    

    # We expand the nodes for each valid column
    for movement in valid_locations:
      match_copy = deepcopy(match)
      
      # Bombs
      if movement[1][0]:								
        if movement[1][1] == "horizontal":			# Horizontal bomb
          match_copy.horizontal_bomb(movement[0])
          bombs[0] = False

        elif movement[1][1] == "vertical":			# Vertical bomb
          match_copy.vertical_bomb(movement[0])	
          bombs[1] = False

        elif movement[1][1] == "classic":			# Classic bomb
          match_copy.classic_bomb(movement[0])
          bombs[2] = False

      else:
        # Move at the current column
        match_copy.move(movement[0], "X")


      # Score for the current move
      new_score = minimax(match_copy, depth-1, alpha, beta, bombs, score_function, True)[2]
      # We check if its the current best (or worst) move	
      if new_score < value:
        value = new_score
        column = movement[0]
        bomb = movement[1]
  
    return column, bomb, value
