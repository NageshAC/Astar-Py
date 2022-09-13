from ast import And
from Node import Node
import numpy as np
from Colors import *
import pygame
from time import sleep

class Grid:

    def __init__(self, order:list, width:int) -> None:
        rows,cols = order
        self.rows  = rows
        self.cols  = cols
        self.width = width

        self.grid = np.array(
            [[Node(r,c,order,width) for c in range(cols)] for r in range(rows)]
        )
        
        for i in self.grid[:,0]: i.cngColor('WALL')
        for i in self.grid[0,:]: i.cngColor('WALL')
        for i in self.grid[-1,:]: i.cngColor('WALL')
        for i in self.grid[:,-1]: i.cngColor('WALL')
 
    def draw(self, win):
        # fill background with Empty color
        bg_color = color_switch['EMT']
        win.fill(bg_color)

        # draw all nodes
        for i in self.grid:
            for j in i:
                j.draw(win)

        # add grid line
        h = self.rows*self.width
        w = self.cols*self.width
        for i in range(self.rows):
            pygame.draw.line(win, GREY, 
                (0, i * self.width), 
                (w, i * self.width)
            ) # Horizontal lines
        for j in range(self.cols):
            pygame.draw.line(win, GREY, 
                (j * self.width, 0), 
                (j * self.width, h)
            ) # Verticle lines

        # update the display
        pygame.display.update()

    def fill_neighbour(self, node, shape):
        Rlimit, Climit = shape
        row,col = node.idx
        if row+1 < Rlimit-1:
            node.neighbors.append(self.grid[row+1, col  ])
        if row-1 > 0:
            node.neighbors.append(self.grid[row-1, col  ])
        if col+1 < Climit-1:
            node.neighbors.append(self.grid[row  , col+1])
        if col-1 > 0:  
            node.neighbors.append(self.grid[row  , col-1])


    def draw_open(self, o, win):
        if o == self.end: return
        o.cngColor('OPEN')
        o.draw(win)
        

    def draw_close(self, c, win):
        if c != self.start and c != self.end:
            c.cngColor('VSTD')
            c.draw(win)
    
    def draw_current(self, c, win):
        if c != self.start and c != self.end:
            c.cngColor('CRT')
            c.draw(win)

    def solve(self, win, start:Node=None, end:Node=None):
        # find start
        if not start:
            for g in self.grid:
                for n in g:
                    if n.is_start():
                        self.start = n
        else: self.start = start

        # find end
        if not end:
            for g in self.grid:
                for n in g:
                    if n.is_end():
                        self.end = n
        else: self.end = end

        open = []
        close = []
        current = self.start

        while current != self.end:
            self.draw_current(current, win)
            # find neighbours
            self.fill_neighbour(current, self.grid.shape)
            # evaluate neighbour score and append to open list
            for n in current.neighbors:
                if n not in close and n not in open and n!=self.start and not n.is_wall():
                    n.evaluate(self.start, self.end)
                    open.append(n)
                    self.draw_open(n, win)
                    n.add_parent(current)
            
            # update the display
            pygame.display.update()

            if not open: return False

            # sorting open list
            open.sort()
            # add current to close list 
            if current != self.start and current != self.end:
                close.append(current)
                self.draw_close(current, win) # --> needs optimisation   
            
            # take the first node from sorted open list and remove it from open list
            current = open[0]
            open.remove(current)     

            sleep(0.1)

        while current.parent:
            if current != self.end and current != self.start:
                current.cngColor('PATH')
                current.draw(win)
            current = current.parent
            
            # update the display
            pygame.display.update()

        return True
