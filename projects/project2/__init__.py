from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, List, overload
import numpy as np
from numpy.typing import NDArray
import copy
from datastructures.array2d import Array2D
import random
from time import sleep
import time
from projects.project2.kbhit import *


class Cell:
    def __init__ (self, status: bool = False) -> None:
        self.status = status #If cell is alive then true, if not then false


    def next_state(self, num_neighbors):
        if num_neighbors < 2:
            self.status = 0
        elif num_neighbors == 3:
            self.status = 1
        elif num_neighbors >= 4:
            self.status = 0
        else:
            pass
    
    @property
    def is_alive(self)->bool: 
        return self.status
    
    @is_alive.setter
    def is_alive(self, alive:bool):
        self.alive = alive

    def __eq__(self,value):
        if isinstance(value,Cell):
            return self.status == value.status
        return False
        
    def __str__(self):
        return "🦠" if self.status else " "
        

class Grid:
    def __init__ (self, rows, cols):
        self.num_rows = rows
        self.num_cols = cols
        self.grid: Array2D = Array2D.empty (rows,cols, data_type=Cell)

        for row in range(rows):
            for col in range (cols):
                self.grid[row][col].is_alive = random.choice([True,False])

    def get_neighbour(self):
        raise NotImplementedError

    def display(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end="")
            print()
        print()


    def nextGeneration (self):
        next_grid = Grid(self.num_rows,self.num_cols) #make empty array
        for row in range(self.num_rows):
            for col in range (self.num_cols):
                num_neighbours = self.get_neighbour(row,col) #implement checking for neighbours here
                next_state = self.grid[row][col].next_state(num_neighbours) #implement rules here
                next_grid[row][col].is_alive = next_state #double check

        return next_grid

    def __eq__(self,value):
        pass
        if isinstance(value,Grid) and self.num_rows == value.num_rows and self.num_cols == value.num_cols:
            return self.grid == value.grid

class GameController:

    #Add all key functions here
    def __init__(self, grid:Grid):
        self.grid = grid
        self.history: List[Grid] = []

    def run(self):
        self.grid.display()

        print("Press 'q' to quit.")

        kbhit = KBHit()

        while True:
            self.grid.display()
            sleep(1)
            if kbhit.kbhit():
                key = kbhit.getch()

                if key == 'q':
                    print("you hit quit")
                    return     



                           
        #Print all Instructions here Ex: [print("Press 'q' to quit.")]
        #account for uppercase and lowercase
        #break will end the loop


        """
        1.Print Grid
        2. loop until break
        3. generate next grid (itereate grid, count neighbours, run rules)
        4.Save current grid to grid history
        5.print grid
        6. set grid = new_grid
        """
