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
        self.num_neighbors = num_neighbors
        if self.num_neighbors < 2:
            self.status = False
        elif self.num_neighbors == 3:
            self.status = True
        elif self.num_neighbors >= 4:
            self.status = False
        else:
            pass
        return self.status
    
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
        return "🦠" if self.status else "⭕"
        

class Grid:
    def __init__ (self, rows, cols):
        self.num_rows = rows
        self.num_cols = cols
        self.grid: Array2D[Cell] = Array2D.empty (rows,cols, data_type=Cell)

        for row in range(rows):
            for col in range (cols):
                self.grid[row][col].status = random.choice([True,False])

    def get_neighbour(self,row_index,col_index)-> int:
        self.neighbours=0
        if row_index != (self.num_rows-1): 
            self.neighbours+=self.notInFirstOrLastCol(row_index,col_index)
            if self.grid[row_index+1][col_index].status == True:
                self.neighbours+=1
            if col_index != (0):
                if self.grid[row_index+1][col_index-1].status == True:
                    self.neighbours+=1
            if col_index != (self.num_cols-1):
                if self.grid[row_index+1][col_index+1].status == True:
                    self.neighbours+=1
        if row_index != 0:
            self.neighbours+=self.notInFirstOrLastCol(row_index,col_index)
            if self.grid[row_index-1][col_index].status == True:
                self.neighbours+=1
            if col_index != (self.num_cols-1):
                if self.grid[row_index-1][col_index+1].status == 1:
                    self.neighbours+=1
            if col_index != 0:
                if self.grid[row_index-1][col_index-1].status == 1:
                    self.neighbours+=1

                    
        return self.neighbours



    def notInFirstOrLastCol(self, row_index, col_index): #a local function I created so I don't have to copy and paste this a ton in my if statement.
        neighboursToo = 0
        if col_index != 0: 
            if self.grid[row_index][col_index-1].status == 1:
                neighboursToo+=1
        if col_index != (self.num_cols-1):
            if self.grid[row_index][col_index+1].status == 1:
                neighboursToo+=1
        return neighboursToo

    def display(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end="")
            print()
        print()


    def nextGeneration (self):
        next_grid = Array2D[Cell].empty(self.num_rows,self.num_cols, data_type=Cell) 
        for row in range(self.num_rows):
            for col in range (self.num_cols):
                num_neighbours = self.get_neighbour(row,col) 
                next_state = self.grid[row][col].next_state(num_neighbours) 
                next_grid[row][col].status = next_state
        return next_grid

        """for row in range(self.num_rows):
            for col in range (self.num_cols):
                self.grid[row][col].status = self.next_grid[row][col].status"""


    def generationEquality(self, generation,history):
        self.history = history
        stability = True
        if self.grid != self.history[generation]:
            stability = False
        """for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col].status != self.history[generation][row][col].status:
                    stability = False """
        return stability

    def __eq__(self,value):
        if isinstance(value,Grid) and self.num_rows == value.num_rows and self.num_cols == value.num_cols:
            return self.grid == value.grid

class GameController:
    def __init__(self, grid:Grid):
        self.grid = grid
        self.history: List[Grid] = []

    def run(self):      
        generation = 0 


        """print("Welcome to Conway's Game of Life!🦠")
        while True:
            if input("What mode would you like? Press '1' for Automatic or '2' for Manual:") == "1":
                self.mode = "A"
                try:
                    self.speed = int(input("What speed in seconds would you like for the program to run?"))
                except ValueError:
                    print("Sorry, I don't understand that...")
                else:
                    print("Press 'Q' to stop the program at any time")
                    break
            if input("What mode would you like? Press '1' for Automatic or '2' for Manual:") == "2":
                self.mode = "M"
                print("Press 'D' to move forward a generation and press 'Q' to quit the program at any time. "
                "The program will automatically end once the colony is stable.")
                break
            else:
                print("Please input a valid number.")""" #Add this back in when fixed

        print("You are on Generation:", generation)
        self.grid.display()        
        kbhit = KBHit()
        while True:

            self.history.append(self.grid)
            """if self.mode == "M":
                if kbhit.kbhit():
                    key = kbhit.getch()
                    if key == 'd' or key == 'D':
                        self.grid.nextGeneration()
                        self.history.append(self.grid)
                        generation+=1
                        print("You are on Generation:", generation)
                        self.grid.display()
                        """"""if len(self.history)>1:
                            stability = self.grid.generationEquality(generation-1,self.history)
                            if stability == True:
                                print("Colony is stable. Terminating simulation.")
                                quit()
                        if len (self.history)>2:
                            stability = True
                            stability = self.grid.generationEquality(generation-2,self.history)
                            if stability == True:
                                print ("Colony is stable. Terminating simulation.")
                                quit()""""""

                    if key == 'q' or key == 'Q':
                        print("You hit quit")
                        return

                if self.mode == "A":
                    while True:
                        sleep(self.speed)
                        self.grid.nextGeneration()
                        self.history.append(self.grid)
                        generation+=1
                        print("You are on Generation:", generation)
                        self.grid.display()                    
                        if kbhit.kbhit():
                            key = kbhit.getch()
                            if key == 'q' or key == 'Q':
                                print("You hit quit")
                                return
                        """"""if len(self.history)>1:
                            stability = self.grid.generationEquality(generation-1,self.history)
                            if stability == True:
                                print("Colony is stable. Terminating simulation.")
                                return
                        if len (self.history)>2:
                            stability = self.grid.generationEquality(generation-2,self.history)
                            if stability == True:
                                print ("Colony is stable. Terminating simulation.")
                                return"""
            self.grid = self.grid.nextGeneration()
            print(self.grid)
            self.history.append(self.grid)
            generation+=1
            self.grid.display()



    """ 1.Print Grid
        2. loop until break
        3. generate next grid (itereate grid, count neighbours, run rules)
        4.Save current grid to grid history
        5.print grid
        6. set grid = new_grid
        """
