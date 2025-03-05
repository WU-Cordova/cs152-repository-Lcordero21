from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy
from datastructures.array2d import Array2D
import random
from time import sleep
import time
if os.name == 'nt':
    import msvcrt


class Cell:
    def __init__(self, row_index, col_index, status) -> None:
        self.row_index = row_index
        self.col_index = col_index
        self.status = status

    def next_state(self, num_neighbors):
        if num_neighbors < 2:
            self.status = 0
        elif num_neighbors == 3:
            self.status = 1
        elif num_neighbors >= 4:
            self.status = 0
        else:
            pass
    
    def aliveCellCheck(self) -> bool: #may not need this function
        return self.status
    
    def is_alive(self):
        pass
    def __eq__(self,value):
        pass
        if isinstance(value,Cell):
            return self.alive == value.alive
        
    #def __str__(self):
        

class Grid:
    def __init__ (self, rows, cols):
        self.num_rows = rows
        self.num_cols = cols
        self.grid: Array2D = Array2D.empty (rows,cols, data_type=Cell)

        for row in range(rows):
            for col in range (cols):
                self.grid[row][col].is_alive = random.choice([True,False])

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end="")
            print()
        print()


    def nextGeneration (self):
        newGen = NDArray() #make empty array

    def __eq__(self,value):
        pass
        #if isinstance(value,Grid) and self.rows == value.rows and self.cols....

class GameController:

    #Add all key functions here
    def __init__(self, grid:Grid):
        self.grid = grid

    def run(self):
        self.grid.display()

        print("Press 'q' to quit.")

        kbhit = KBHit()

        while True:
            sleep(1)
            if kbhit.kbhit():
                key = kbhit.getch()

                if key == 'q':
                    print("you hit quit")
                    return                    
        #Print all Instructions here Ex: [print("Press 'q' to quit.")]
        #account for uppercase and lowercase
