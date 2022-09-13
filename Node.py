import numpy as np
from Colors import *
import pygame

def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

class Node:

    def __init__(self, row:int, col:int, order:list, width:int) -> None:
        # print(f'creating({row},{col})')
        self.idx        = np.array([row,col])
        self.loc        = np.array([col*width,row*width])
        self.width      = width
        self.color      = WHITE
        self.parent     = None
        self.neighbors  = []
        self.gscore     = 0
        self.fscore     = float('inf')
    
    def cngColor(self, mode:str):
        self.color = color_switch[mode]

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.loc[0]+1, self.loc[1]+1, self.width-1, self.width-1))

    def is_empty(self): return self.color == color_switch['EMT']
    def is_wall(self): return self.color == color_switch['WALL']
    def is_start(self): return self.color == color_switch['SRC']
    def is_end(self): return self.color == color_switch['DEST']

    def add_neighbour(self, neighbour): self.neighbors.append(neighbour)
    def add_parent(self, parent): 
        if self.parent == None or parent.gscore < self.parent.gscore:
            self.parent = parent
    
    def evaluate(self, start, end):
        self.gscore = distance(start.idx, self.idx)
        self.escore = distance(self.idx, end.idx)
        self.fscore = self.gscore + self.escore

    def __lt__(self, other):
        if self.fscore < other.fscore: return True
        elif self.fscore == other.fscore: return self.gscore > other.gscore
        return False
        # if self.escore < other.escore: return True
        # elif self.escore == other.escore: return self.gscore > other.gscore


