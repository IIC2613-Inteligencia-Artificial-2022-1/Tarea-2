from cube import RCube 

def example_heuristic(state):
    '''Heurística de ejemplo, cuenta diferencias entre cubo inicial y final'''
    dif  = 0 
    for i in range(len(state)):
        if RCube.sol[i] != state[i]:
            dif += 1
    return dif


def max_manhattan_corners(state):
    '''TODO'''
    pass


def min_manhattan_corners(state):
    '''TODO'''
    pass


def sum_manhattan_corners(state):
    '''TODO'''
    pass
