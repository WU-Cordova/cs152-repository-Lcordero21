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

    def get_neighbour(self):
        raise NotImplementedError

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end="")
            print()
        print()


    def nextGeneration (self):
        newGen = Grid(self.rows,self.cols) #make empty array
        for row in range(self.rows):
            for col in range (self.cols):
                num_neighbours = self.get_neighbour(row,col) #implement checking for neighbours here
                next_state = self.grid[row][col].next_state(num_neighbours) #implement rules here
                next_grid[row][col].is_alive = next_state #double check

        return next_grid

    def __eq__(self,value):
        pass
        #if isinstance(value,Grid) and self.rows == value.rows and self.cols....

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
