import heuristics
import random
import time
import sys

from cube import RCube
from binary_heap import BinaryHeap
from node import Node


class Astar(object):
    def __init__(self, initial_state, heuristic = None):
        super(Astar, self).__init__()
        self.expansions = 0
        self.generated = 0
        self.cube = RCube(RCube.sol)
        self.cube_string = self.cube.flat_str()
        self.initial_state = initial_state
        self.heuristic = heuristic if heuristic else heuristics.example_heuristic
        self.open = BinaryHeap()
        self.closed_ = []

    def search(self):
        '''Implementar'''
        pass




        