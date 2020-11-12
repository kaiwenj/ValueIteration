import sys
sys.path.append('../src/')
import unittest
from ddt import ddt, data, unpack
import ValueIteration as targetCode #change to file name


@ddt
class TestValueIteration(unittest.TestCase):
    def setUp(self): 
        # for the deterministic transition, goal state is (1,1), trap state is (1,2). The board is 3 (0,1,2) by 5 (0,1,2,3,4)
        # All states the same number of moves away from (1,1) that avoid traveling through the trap state will have the same value
        self.deterministicTransitionTable = {(0, 0): {(1, 0): {(1, 0): 1},(0, 1): {(0, 1): 1},(-1, 0): {(0, 0): 1},(0, -1): {(0, 0): 1},(0, 0): {(0, 0): 1}},(0, 1): {(1, 0): {(1, 1): 1},(0, 1): {(0, 2): 1},(-1, 0): {(0, 1): 1},(0, -1): {(0, 0): 1},(0, 0): {(0, 1): 1}},(0, 2): {(1, 0): {(1, 2): 1},(0, 1): {(0, 3): 1},(-1, 0): {(0, 2): 1},(0, -1): {(0, 1): 1},(0, 0): {(0, 2): 1}},(0, 3): {(1, 0): {(1, 3): 1},(0, 1): {(0, 4): 1},(-1, 0): {(0, 3): 1},(0, -1): {(0, 2): 1},(0, 0): {(0, 3): 1}},(0, 4): {(1, 0): {(1, 4): 1},(0, 1): {(0, 4): 1},(-1, 0): {(0, 4): 1},(0, -1): {(0, 3): 1},(0, 0): {(0, 4): 1}},(1, 0): {(1, 0): {(2, 0): 1},(0, 1): {(1, 1): 1},(-1, 0): {(0, 0): 1},(0, -1): {(1, 0): 1},(0, 0): {(1, 0): 1}},(1, 1): {(1, 0): {(2, 1): 1},(0, 1): {(1, 2): 1},(-1, 0): {(0, 1): 1},(0, -1): {(1, 0): 1},(0, 0): {(1, 1): 1}},(1, 2): {(1, 0): {(2, 2): 1},(0, 1): {(1, 3): 1},(-1, 0): {(0, 2): 1},(0, -1): {(1, 1): 1},(0, 0): {(1, 2): 1}},(1, 3): {(1, 0): {(2, 3): 1},(0, 1): {(1, 4): 1},(-1, 0): {(0, 3): 1},(0, -1): {(1, 2): 1},(0, 0): {(1, 3): 1}},(1, 4): {(1, 0): {(2, 4): 1},(0, 1): {(1, 4): 1},(-1, 0): {(0, 4): 1},(0, -1): {(1, 3): 1},(0, 0): {(1, 4): 1}},(2, 0): {(1, 0): {(2, 0): 1},(0, 1): {(2, 1): 1},(-1, 0): {(1, 0): 1},(0, -1): {(2, 0): 1},(0, 0): {(2, 0): 1}},(2, 1): {(1, 0): {(2, 1): 1},(0, 1): {(2, 2): 1},(-1, 0): {(1, 1): 1},(0, -1): {(2, 0): 1},(0, 0): {(2, 1): 1}},(2, 2): {(1, 0): {(2, 2): 1},(0, 1): {(2, 3): 1},(-1, 0): {(1, 2): 1},(0, -1): {(2, 1): 1},(0, 0): {(2, 2): 1}},(2, 3): {(1, 0): {(2, 3): 1},(0, 1): {(2, 4): 1},(-1, 0): {(1, 3): 1},(0, -1): {(2, 2): 1},(0, 0): {(2, 3): 1}},(2, 4): {(1, 0): {(2, 4): 1},(0, 1): {(2, 4): 1},(-1, 0): {(1, 4): 1},(0, -1): {(2, 3): 1},(0, 0): {(2, 4): 1}}}
        self.deterministicRewardTable = {(0, 0): {(1, 0): {(1, 0): -1},(0, 1): {(0, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 0): -0.1}},(0, 1): {(1, 0): {(1, 1): -1},(0, 1): {(0, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 1): -0.1}},(0, 2): {(1, 0): {(1, 2): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(0, 1): -1},(0, 0): {(0, 2): -0.1}},(0, 3): {(1, 0): {(1, 3): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(0, 2): -1},(0, 0): {(0, 3): -1}},(0, 4): {(1, 0): {(1, 4): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 4): -1},(0, -1): {(0, 3): -1},(0, 0): {(0, 4): -0.1}},(1, 0): {(1, 0): {(2, 0): -1},(0, 1): {(1, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 0): -0.1}},(1, 1): {(1, 0): {(2, 1): 9},(0, 1): {(1, 2): 9},(-1, 0): {(0, 1): 9},(0, -1): {(1, 0): 9},(0, 0): {(1, 1): 9.9}},(1, 2): {(1, 0): {(2, 2): -100},(0, 1): {(1, 3): -100},(-1, 0): {(0, 2): -100},(0, -1): {(1, 1): -100},(0, 0): {(1, 2): -100}},(1, 3): {(1, 0): {(2, 3): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(1, 2): -1},(0, 0): {(1, 3): -0.1}},(1, 4): {(1, 0): {(2, 4): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 4): -1},(0, -1): {(1, 3): -1},(0, 0): {(1, 4): -0.1}},(2, 0): {(1, 0): {(2, 0): -1},(0, 1): {(2, 1): -1},(-1, 0): {(1, 0): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 0): -0.1}},(2, 1): {(1, 0): {(2, 1): -1},(0, 1): {(2, 2): -1},(-1, 0): {(1, 1): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 1): -0.1}},(2, 2): {(1, 0): {(2, 2): -1},(0, 1): {(2, 3): -1},(-1, 0): {(1, 2): -1},(0, -1): {(2, 1): -1},(0, 0): {(2, 2): -0.1}},(2, 3): {(1, 0): {(2, 3): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 3): -1},(0, -1): {(2, 2): -1},(0, 0): {(2, 3): -0.1}},(2, 4): {(1, 0): {(2, 4): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 4): -1},(0, -1): {(2, 3): -1},(0, 0): {(2, 4): -0.1}}}
        self.determinsiticValueTable = {(i, j):0 for i in range(3) for j in range(5)}
        self.uniformV={(i, j):20 for i in range(3) for j in range(5)}
        self.goalTrapV={(i, j):0 for i in range(3) for j in range(5)}
        self.goalTrapV[(1,2)]=-100
        self.goalTrapV[(1,1)]=100
        self.deterministicTransitionFunction=lambda s, a, sPrime: self.deterministicTransitionTable.get(s).get(a).get(sPrime, 0)
        self.deterministicRewardFunction=lambda s, a, sPrime: self.deterministicRewardTable.get(s).get(a).get(sPrime, 0)
        self.stateSpace=list(self.deterministicTransitionTable.keys())
        self.actionSpaceFunction=lambda s: list(self.deterministicTransitionTable.get(s).keys())
        
		# For the slippery transition, the goal state is (3,1), trap state is (1,1). The board is 4 by 4
		# Visualizations of the exact slip directions sampled for this transition can be found in the accompanying demo ipynb
        self.slipperyTransitionTable = {(0,0): {(1, 0): {(1, 0): 0.7,(0, 1): 0.20000000000000004,(0, 0): 0.10000000000000002}, (0, 1): {(0, 1): 0.7999999999999999,(1, 0): 0.20000000000000004}, (-1, 0): {(0, 0): 0.7,(1, 0): 0.20000000000000004,(0, 1): 0.10000000000000002}, (0, -1): {(0, 0): 0.7,(1, 0): 0.10000000000000002,(0, 1): 0.20000000000000004}, (0, 0): {(0, 0): 0.7999999999999999,(0, 1): 0.10000000000000002,(1, 0): 0.10000000000000002}},(0,1): {(1, 0): {(1, 1): 0.7,(0, 0): 0.10000000000000002,(0, 2): 0.10000000000000002,(0, 1): 0.10000000000000002}, (0, 1): {(0, 2): 0.7,(0, 1): 0.10000000000000002,(0, 0): 0.20000000000000004}, (-1, 0): {(0, 1): 0.7999999999999999,(0, 2): 0.10000000000000002,(0, 0): 0.10000000000000002}, (0, -1): {(0, 0): 0.8999999999999999,(0, 1): 0.10000000000000002}, (0, 0): {(0, 1): 0.7999999999999999,(0, 2): 0.10000000000000002,(0, 0): 0.10000000000000002}},(0, 2): {(1, 0): {(1, 2): 0.7999999999999999, (0, 3): 0.20000000000000004},(0, 1): {(0, 3): 0.7, (0, 1): 0.30000000000000004},(-1, 0): {(0, 2): 0.7,(0, 3): 0.20000000000000004,(1, 2): 0.10000000000000002},(0, -1): {(0, 1): 0.7,(0, 2): 0.20000000000000004,(1, 2): 0.10000000000000002},(0, 0): {(0, 2): 0.7,(1, 2): 0.20000000000000004,(0, 1): 0.10000000000000002}},(0,3): {(1, 0): {(1, 3): 0.7999999999999999,(0, 2): 0.10000000000000002,(0, 3): 0.10000000000000002}, (0, 1): {(0, 3): 0.9999999999999999}, (-1,0): {(0, 3): 0.7999999999999999,(1, 3): 0.10000000000000002,(0, 2): 0.10000000000000002}, (0, -1): {(0, 2): 0.7999999999999999,(1, 3): 0.20000000000000004}, (0, 0): {(0, 3): 0.7,(0, 2): 0.10000000000000002,(1, 3): 0.20000000000000004}},(1,0): {(1, 0): {(2, 0): 0.7,(0, 0): 0.10000000000000002,(1, 0): 0.10000000000000002,(1, 1): 0.10000000000000002}, (0, 1): {(1, 1): 0.7999999999999999,(2, 0): 0.10000000000000002,(1, 0): 0.10000000000000002}, (-1, 0): {(0, 0): 0.7,(1, 1): 0.10000000000000002,(2, 0): 0.20000000000000004}, (0, -1): {(1, 0): 0.7999999999999999,(0, 0): 0.20000000000000004}, (0, 0): {(1, 0): 0.7999999999999999,(1, 1): 0.10000000000000002,(0, 0): 0.10000000000000002}},(1, 1): {(1, 0): {(2, 1): 0.8999999999999999, (1, 0): 0.10000000000000002},(0, 1): {(1, 2): 0.7999999999999999,(1, 0): 0.10000000000000002,(1, 1): 0.10000000000000002},(-1, 0): {(0, 1): 0.8999999999999999, (1, 2): 0.10000000000000002},(0, -1): {(1, 0): 0.7,(0, 1): 0.10000000000000002,(1, 2): 0.20000000000000004},(0, 0): {(1, 1): 0.7,(1, 2): 0.10000000000000002,(2, 1): 0.10000000000000002,(1, 0): 0.10000000000000002}},(1,2): {(1, 0): {(2, 2): 0.7999999999999999,(1, 3): 0.10000000000000002,(0, 2): 0.10000000000000002}, (0, 1): {(1, 3): 0.8999999999999999,(0, 2): 0.10000000000000002}, (-1, 0): {(0, 2): 0.7,(1, 2): 0.10000000000000002,(2, 2): 0.10000000000000002,(1, 3): 0.10000000000000002}, (0, -1): {(1, 1): 0.7999999999999999,(2, 2): 0.20000000000000004}, (0, 0): {(1, 2): 0.7,(2, 2): 0.20000000000000004,(1, 1): 0.10000000000000002}},(1,3): {(1, 0): {(2, 3): 0.7,(0, 3): 0.20000000000000004,(1, 2): 0.10000000000000002}, (0, 1): {(1, 3): 0.7,(2, 3): 0.20000000000000004,(0, 3): 0.10000000000000002}, (-1, 0): {(0, 3): 0.8999999999999999,(2, 3): 0.10000000000000002}, (0, -1): {(1, 2): 0.8999999999999999,(1, 3): 0.10000000000000002}, (0, 0): {(1, 3): 0.7999999999999999,(0, 3): 0.10000000000000002,(1, 2): 0.10000000000000002}},(2,0): {(1, 0): {(3, 0): 0.7,(2, 0): 0.20000000000000004,(1, 0): 0.10000000000000002}, (0, 1): {(2, 1): 0.7,(2, 0): 0.20000000000000004,(1, 0): 0.10000000000000002}, (-1, 0): {(1, 0): 0.7,(2, 0): 0.20000000000000004,(3, 0): 0.10000000000000002}, (0, -1): {(2, 0): 0.7999999999999999,(2, 1): 0.10000000000000002,(3, 0): 0.10000000000000002}, (0, 0): {(2, 0): 0.7,(3, 0): 0.10000000000000002,(1, 0): 0.20000000000000004}},(2,1): {(1, 0): {(3, 1): 0.7999999999999999,(2, 1): 0.10000000000000002,(1, 1): 0.10000000000000002}, (0, 1): {(2, 2): 0.7999999999999999,(2, 0): 0.10000000000000002,(3, 1): 0.10000000000000002}, (-1, 0): {(1, 1): 0.7,(2, 2): 0.20000000000000004,(3, 1): 0.10000000000000002}, (0, -1): {(2, 0): 0.7,(3, 1): 0.10000000000000002,(1, 1): 0.10000000000000002,(2, 2): 0.10000000000000002}, (0, 0): {(2, 1): 0.7,(2, 2): 0.30000000000000004}},(2,2): {(1, 0): {(3, 2): 0.7,(2, 2): 0.20000000000000004,(2, 1): 0.10000000000000002}, (0, 1): {(2, 3): 0.7999999999999999,(2, 2): 0.20000000000000004}, (-1, 0): {(1, 2): 0.7,(2, 1): 0.10000000000000002,(2, 2): 0.10000000000000002,(3, 2): 0.10000000000000002}, (0, -1): {(2, 1): 0.7999999999999999,(2, 2): 0.10000000000000002,(2, 3): 0.10000000000000002}, (0, 0): {(2, 2): 0.7999999999999999,(3, 2): 0.10000000000000002,(1, 2): 0.10000000000000002}},(2,3): {(1, 0): {(3, 3): 0.7,(1, 3): 0.20000000000000004,(2, 2): 0.10000000000000002}, (0, 1): {(2, 3): 0.7999999999999999,(1, 3): 0.10000000000000002,(3, 3): 0.10000000000000002}, (-1, 0): {(1, 3): 0.7999999999999999,(2, 3): 0.10000000000000002,(2, 2): 0.10000000000000002}, (0, -1): {(2, 2): 0.7,(3, 3): 0.10000000000000002,(1, 3): 0.10000000000000002,(2, 3): 0.10000000000000002}, (0, 0): {(2, 3): 0.8999999999999999,(3, 3): 0.10000000000000002}},(3,0): {(1, 0): {(3, 0): 0.7999999999999999,(3, 1): 0.10000000000000002,(2, 0): 0.10000000000000002}, (0, 1): {(3, 1): 0.7999999999999999,(3, 0): 0.20000000000000004}, (-1, 0): {(2, 0): 0.7999999999999999,(3, 1): 0.20000000000000004}, (0, -1): {(3, 0): 0.8999999999999999,(3, 1): 0.10000000000000002}, (0, 0): {(3, 0): 0.7999999999999999,(3, 1): 0.10000000000000002,(2, 0): 0.10000000000000002}},(3,1): {(1, 0): {(3, 1): 0.7,(3, 2): 0.20000000000000004,(2, 1): 0.10000000000000002}, (0, 1): {(3, 2): 0.8999999999999999,(3, 0): 0.10000000000000002}, (-1, 0): {(2, 1): 0.7,(3, 1): 0.20000000000000004,(3, 0): 0.10000000000000002}, (0, -1): {(3, 0): 0.7999999999999999,(3, 1): 0.10000000000000002,(2, 1): 0.10000000000000002}, (0, 0): {(3, 1): 0.7999999999999999,(3, 0): 0.10000000000000002,(3, 2): 0.10000000000000002}},(3,2): {(1, 0): {(3, 2): 0.7999999999999999,(3, 1): 0.10000000000000002,(2, 2): 0.10000000000000002}, (0, 1): {(3, 3): 0.7999999999999999,(3, 1): 0.20000000000000004}, (-1, 0): {(2, 2): 0.7,(3, 2): 0.10000000000000002,(3, 3): 0.10000000000000002,(3, 1): 0.10000000000000002}, (0, -1): {(3, 1): 0.7999999999999999,(2, 2): 0.10000000000000002,(3, 3): 0.10000000000000002}, (0, 0): {(3, 2): 0.7,(3, 3): 0.20000000000000004,(3, 1): 0.10000000000000002}},(3, 3): {(1, 0): {(3, 3): 0.7, (2, 3): 0.30000000000000004},(0, 1): {(3, 3): 0.7,(3, 2): 0.10000000000000002,(2, 3): 0.20000000000000004},(-1, 0): {(2, 3): 0.7999999999999999,(3, 2): 0.10000000000000002,(3, 3): 0.10000000000000002},(0, -1): {(3, 2): 0.8999999999999999, (3, 3): 0.10000000000000002},(0, 0): {(3, 3): 0.7999999999999999, (3, 2): 0.20000000000000004}}}
        self.slipperyRewardTable = {(0, 0): {(1, 0): {(1, 0): -1, (0, 1): -1, (0, 0): -1},(0, 1): {(0, 1): -1, (1, 0): -1},(-1, 0): {(0, 0): -1, (1, 0): -1, (0, 1): -1},(0, -1): {(0, 0): -1, (1, 0): -1, (0, 1): -1},(0, 0): {(0, 0): -0.1, (0, 1): -0.1, (1, 0): -0.1}},(0, 1): {(1, 0): {(1, 1): -1, (0, 0): -1, (0, 2): -1, (0, 1): -1},(0, 1): {(0, 2): -1, (0, 1): -1, (0, 0): -1},(-1, 0): {(0, 1): -1, (0, 2): -1, (0, 0): -1},(0, -1): {(0, 0): -1, (0, 1): -1},(0, 0): {(0, 1): -1, (0, 2): -1, (0, 0): -1}},(0, 2): {(1, 0): {(1, 2): -1, (0, 3): -1},(0, 1): {(0, 3): -1, (0, 1): -1},(-1, 0): {(0, 2): -1, (0, 3): -1, (1, 2): -1},(0, -1): {(0, 1): -1, (0, 2): -1, (1, 2): -1},(0, 0): {(0, 2): -0.1, (1, 2): -0.1, (0, 1): -0.1}},(0, 3): {(1, 0): {(1, 3): -1, (0, 2): -1, (0, 3): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 3): -1, (1, 3): -1, (0, 2): -1},(0, -1): {(0, 2): -1, (1, 3): -1},(0, 0): {(0, 3): -0.1, (0, 2): -0.1, (1, 3): -0.1}},(1, 0): {(1, 0): {(2, 0): -1, (0, 0): -1, (1, 0): -1, (1, 1): -1},(0, 1): {(1, 1): -1, (2, 0): -1, (1, 0): -1},(-1, 0): {(0, 0): -1, (1, 1): -1, (2, 0): -1},(0, -1): {(1, 0): -1, (0, 0): -1},(0, 0): {(1, 0): -0.1, (1, 1): -0.1, (0, 0): -0.1}},(1, 1): {(1, 0): {(2, 1): -100, (1, 0): -100},(0, 1): {(1, 2): -100, (1, 0): -100, (1, 1): -100},(-1, 0): {(0, 1): -100, (1, 2): -100},(0, -1): {(1, 0): -100, (0, 1): -100, (1, 2): -100},(0, 0): {(1, 1): -100, (1, 2): -100, (2, 1): -100, (1, 0): -100}},(1, 2): {(1, 0): {(2, 2): -1, (1, 3): -1, (0, 2): -1},(0, 1): {(1, 3): -1, (0, 2): -1},(-1, 0): {(0, 2): -1, (1, 2): -1, (2, 2): -1, (1, 3): -1},(0, -1): {(1, 1): -1, (2, 2): -1},(0, 0): {(1, 2): -0.1, (2, 2): -0.1, (1, 1): -0.1}},(1, 3): {(1, 0): {(2, 3): -1, (0, 3): -1, (1, 2): -1},(0, 1): {(1, 3): -1, (2, 3): -1, (0, 3): -1},(-1, 0): {(0, 3): -1, (2, 3): -1},(0, -1): {(1, 2): -1, (1, 3): -1},(0, 0): {(1, 3): -0.1, (0, 3): -0.1, (1, 2): -0.1}},(2, 0): {(1, 0): {(3, 0): -1, (2, 0): -1, (1, 0): -1},(0, 1): {(2, 1): -1, (2, 0): -1, (1, 0): -1},(-1, 0): {(1, 0): -1, (2, 0): -1, (3, 0): -1},(0, -1): {(2, 0): -1, (2, 1): -1, (3, 0): -1},(0, 0): {(2, 0): -0.1, (3, 0): -0.1, (1, 0): -0.1}},(2, 1): {(1, 0): {(3, 1): -1, (2, 1): -1, (1, 1): -1},(0, 1): {(2, 2): -1, (2, 0): -1, (3, 1): -1},(-1, 0): {(1, 1): -1, (2, 2): -1, (3, 1): -1},(0, -1): {(2, 0): -1, (3, 1): -1, (1, 1): -1, (2, 2): -1},(0, 0): {(2, 1): -0.1, (2, 2): -0.1}},(2, 2): {(1, 0): {(3, 2): -1, (2, 2): -1, (2, 1): -1},(0, 1): {(2, 3): -1, (2, 2): -1},(-1, 0): {(1, 2): -1, (2, 1): -1, (2, 2): -1, (3, 2): -1},(0, -1): {(2, 1): -1, (2, 2): -1, (2, 3): -1},(0, 0): {(2, 2): -0.1, (3, 2): -0.1, (1, 2): -0.1}},(2, 3): {(1, 0): {(3, 3): -1, (1, 3): -1, (2, 2): -1},(0, 1): {(2, 3): -1, (1, 3): -1, (3, 3): -1},(-1, 0): {(1, 3): -1, (2, 3): -1, (2, 2): -1},(0, -1): {(2, 2): -1, (3, 3): -1, (1, 3): -1, (2, 3): -1},(0, 0): {(2, 3): -0.1, (3, 3): -0.1}},(3, 0): {(1, 0): {(3, 0): -1, (3, 1): -1, (2, 0): -1},(0, 1): {(3, 1): -1, (3, 0): -1},(-1, 0): {(2, 0): -1, (3, 1): -1},(0, -1): {(3, 0): -1, (3, 1): -1},(0, 0): {(3, 0): -0.1, (3, 1): -0.1, (2, 0): -0.1}},(3, 1): {(1, 0): {(3, 1): 9, (3, 2): 9, (2, 1): 9},(0, 1): {(3, 2): 9, (3, 0): 9},(-1, 0): {(2, 1): 9, (3, 1): 9, (3, 0): 9},(0, -1): {(3, 0): 9, (3, 1): 9, (2, 1): 9},(0, 0): {(3, 1): 9.9, (3, 0): 9.9, (3, 2): 9.9}},(3, 2): {(1, 0): {(3, 2): -1, (3, 1): -1, (2, 2): -1},(0, 1): {(3, 3): -1, (3, 1): -1},(-1, 0): {(2, 2): -1, (3, 2): -1, (3, 3): -1, (3, 1): -1},(0, -1): {(3, 1): -1, (2, 2): -1, (3, 3): -1},(0, 0): {(3, 2): -0.1, (3, 3): -0.1, (3, 1): -0.1}},(3, 3): {(1, 0): {(3, 3): -1, (2, 3): -1},(0, 1): {(3, 3): -1, (3, 2): -1, (2, 3): -1},(-1, 0): {(2, 3): -1, (3, 2): -1, (3, 3): -1},(0, -1): {(3, 2): -1, (3, 3): -1},(0, 0): {(3, 3): -0.1, (3, 2): -0.1}}}
        self.slipperyValueTable = {state:0 for state in self.slipperyRewardTable.keys()}
        self.slipperyTransitionFunction=lambda s, a, sPrime: self.slipperyTransitionTable.get(s).get(a).get(sPrime, 0)
        self.slipperyRewardFunction=lambda s, a, sPrime: self.slipperyRewardTable.get(s).get(a).get(sPrime, 0)
        self.slipperyStateSpace=list(self.slipperyTransitionTable.keys())
        self.slipperyActionSpaceFunction=lambda s: list(self.slipperyTransitionTable.get(s).keys())
        self.slipperyV={(i, j):0 for i in range(4) for j in range(4)}
        self.slipperyUniformV={(i, j):20 for i in range(4) for j in range(4)}
        self.slipperyTrapV={(i, j):0 for i in range(4) for j in range(4)}
        self.slipperyTrapV[(1,1)]=-100
        self.slipperyTrapV[(3,1)]=100
        self.convergenceTolerance = .000001
        self.gamma = .9
        
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
            
        
    @data(((0,0), -0.1))
    @unpack
    def testBellmanUpdateCornerZeroV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                               self.deterministicRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.determinsiticValueTable)
        self.assertAlmostEqual(calculatedResult, expectedResult)
    
    @data(((1,1), 9.9))
    @unpack
    def testBellmanUpdateGoalZeroV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                               self.deterministicRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.determinsiticValueTable)
        self.assertAlmostEqual(calculatedResult, expectedResult)

    @data(((1,2), -100))
    @unpack
    def testBellmanUpdateTrapZeroV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                               self.deterministicRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.determinsiticValueTable)
        self.assertAlmostEqual(calculatedResult, expectedResult)

    @data(((0,0), 17.9))
    @unpack
    def testBellmanUpdateCornerUniformV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                               self.deterministicRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.uniformV)
        self.assertAlmostEqual(calculatedResult, expectedResult)
        
    @data(((0,1), 89))
    @unpack
    def testBellmanUpdateCornerGoalV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                               self.deterministicRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.goalTrapV)
        self.assertAlmostEqual(calculatedResult, expectedResult)
        
    @data(((1,2), -10))
    @unpack
    def testBellmanUpdateCornerTrapV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                               self.deterministicRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.goalTrapV)
        self.assertAlmostEqual(calculatedResult, expectedResult) 
    
    @data(((0,0), -0.1))
    @unpack
    def testBellmanUpdateSlipperyV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.slipperyStateSpace, self.slipperyActionSpaceFunction, self.slipperyTransitionFunction,\
                                               self.slipperyRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.slipperyV)
        self.assertAlmostEqual(calculatedResult, expectedResult) 
        
    @data(((0,0), 17.9))
    @unpack
    def testBellmanUpdateSlipperyUniformV(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.slipperyStateSpace, self.slipperyActionSpaceFunction, self.slipperyTransitionFunction,\
                                               self.slipperyRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.slipperyUniformV)
        self.assertAlmostEqual(calculatedResult, expectedResult) 
    
    @data(((0,1), -1))
    @unpack
    def testBellmanUpdateSlipperyTrapVNearTrap(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.slipperyStateSpace, self.slipperyActionSpaceFunction, self.slipperyTransitionFunction,\
                                               self.slipperyRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.slipperyTrapV)
        self.assertAlmostEqual(calculatedResult, expectedResult) 
    
    @data(((2,1), 62))
    @unpack
    def testBellmanUpdateSlipperyTrapVNearGoal(self, s, expectedResult):
        bellmanUpdate=targetCode.BellmanUpdate(self.slipperyStateSpace, self.slipperyActionSpaceFunction, self.slipperyTransitionFunction,\
                                               self.slipperyRewardFunction, self.gamma)
        calculatedResult=bellmanUpdate(s, self.slipperyTrapV)
        self.assertAlmostEqual(calculatedResult, expectedResult)
        
 
    @data(((0,0), {(0, 0):1}))
    @unpack
    def testPlainPolicy(self, s, expectedResult):
        getPolicy=targetCode.GetPolicy(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                       self.deterministicRewardFunction, self.gamma, self.determinsiticValueTable, 10e-7)
        calculatedResult=getPolicy(s)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult)
    
    @data(((1,2), {(0, -1):1}))
    @unpack
    def testDetPolicy(self, s, expectedResult):
        getPolicy=targetCode.GetPolicy(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                       self.deterministicRewardFunction, self.gamma, self.goalTrapV, 10e-7)
        calculatedResult=getPolicy(s)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult)
        
    @data(((0,3), {(0, -1):0.2, (0, 1):0.2, (0, 0):0.2, (1, 0):0.2, (-1, 0):0.2}))
    @unpack
    def testStochasticPolicy(self, s, expectedResult):
        getPolicy=targetCode.GetPolicy(self.stateSpace, self.actionSpaceFunction, self.deterministicTransitionFunction,\
                                       self.deterministicRewardFunction, self.gamma, self.goalTrapV, 10e-7)
        calculatedResult=getPolicy(s)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult)
    
    @data(((2,1), {(1, 0):1}))
    @unpack
    def testSlipperyDetPolicy(self, s, expectedResult):
        getPolicy=targetCode.GetPolicy(self.slipperyStateSpace, self.slipperyActionSpaceFunction, self.slipperyTransitionFunction,\
                                       self.slipperyRewardFunction, self.gamma, self.slipperyTrapV, 10e-7)
        calculatedResult=getPolicy(s)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult)
    
    @data(((0,1), {(0, -1):0.25, (0, 1):0.25, (0, 0):0.25, (-1, 0):0.25}))
    @unpack
    def testSlipperyStochasticPolicy(self, s, expectedResult):
        getPolicy=targetCode.GetPolicy(self.slipperyStateSpace, self.slipperyActionSpaceFunction, self.slipperyTransitionFunction,\
                                       self.slipperyRewardFunction, self.gamma, self.slipperyTrapV, 10e-7)
        calculatedResult=getPolicy(s)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult)
    
    def tearDown(self):
        pass
 
if __name__ == '__main__':
	unittest.main(verbosity=2)
