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
        self.status = status 
    #Note: If the cell is alive then it is true, if it is not then it is false.

    #The following will calculate the next status of a cell based on the number of neighbours it has.
    def next_state(self, num_neighbors, status):
        new_status = status
        if num_neighbors < 2:
            new_status = False
        elif num_neighbors == 3:
            new_status = True
        elif num_neighbors >= 4:
            new_status = False
        else:
            pass
        return new_status
    
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


    #The following function will return the number of neighbours a cell has
    def get_neighbour(self,row_index,col_index)-> int: 
        self.neighbours=0
        if row_index == 0: 
            self.neighbours+=self.inFirstOrLastCol(row_index,col_index)
            if self.grid[row_index+1][col_index].status == True:
                self.neighbours+=1
            if col_index != (0):
                if self.grid[row_index+1][col_index-1].status == True:
                    self.neighbours+=1
            if col_index != (self.num_cols-1):
                if self.grid[row_index+1][col_index+1].status == True:
                    self.neighbours+=1
        elif row_index == (self.num_rows-1):
            self.neighbours+=self.inFirstOrLastCol(row_index,col_index)
            if self.grid[row_index-1][col_index].status == True:
                self.neighbours+=1
            if col_index != (self.num_cols-1):
                if self.grid[row_index-1][col_index+1].status == 1:
                    self.neighbours+=1
            if col_index != 0:
                if self.grid[row_index-1][col_index-1].status == 1:
                    self.neighbours+=1
        else:
            self.neighbours+=self.inFirstOrLastCol(row_index, col_index)
            if self.grid[row_index+1][col_index].status == True:
                self.neighbours+=1
            if col_index != (0):
                if self.grid[row_index+1][col_index-1].status == True:
                    self.neighbours+=1
            if col_index != (self.num_cols-1):
                if self.grid[row_index+1][col_index+1].status == True:
                    self.neighbours+=1
            if self.grid[row_index-1][col_index].status == True:
                self.neighbours+=1
            if col_index != (self.num_cols-1):
                if self.grid[row_index-1][col_index+1].status == 1:
                    self.neighbours+=1
            if col_index != 0:
                if self.grid[row_index-1][col_index-1].status == 1:
                    self.neighbours+=1
        return self.neighbours


    #A tiny function I created so I don't have to copy and paste this a ton in my if statement in "get_neighbour".
    def inFirstOrLastCol(self, row_index, col_index): 
        neighboursToo = 0
        if col_index == (self.num_cols - 1): 
            if self.grid[row_index][col_index-1].status == 1:
                neighboursToo+=1
        elif col_index == 0:
            if self.grid[row_index][col_index+1].status == 1:
                neighboursToo+=1
        elif (col_index != (self.num_cols -1)) and (col_index != 0):
            if self.grid[row_index][col_index-1].status == 1:
                neighboursToo+=1
            if self.grid[row_index][col_index+1].status == 1:
                neighboursToo+=1
        return neighboursToo

    #The following function will display the grid
    def display(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end="")
            print()
        print()

    #The following function will generate the next generation
    def nextGeneration (self):
        next_grid = Array2D.empty(self.num_rows,self.num_cols, data_type=Cell) 
        self.old_grid = copy.deepcopy(self.grid)
        for row in range(self.num_rows):
            for col in range (self.num_cols):
                num_neighbours = self.get_neighbour(row,col) 
                next_state = self.old_grid[row][col].next_state(num_neighbours, self.old_grid[row][col].status) 
                next_grid[row][col].status = next_state
        self.grid = next_grid


    #The following function is the main player in determining if a colony is repeating
    def generationEquality(self, item):
        stability = True       
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col].status != item[row][col].status:
                    stability = False 
        return stability

    def __eq__(self,value):
        if isinstance(value,Grid) and self.num_rows == value.num_rows and self.num_cols == value.num_cols:
            return self.grid == value.grid

class GameController:
    def __init__(self, grid:Grid):
        self.grid = grid
        self.history: List[Grid] = []

    def run(self):      
        #initializes generation 0 and asks the user what mode they would like
        generation = 0 
        print("Welcome to Conway's Game of Life!🦠")
        gameMode = input("What mode would you like? Press '1' for Automatic or '2' for Manual:")
        while True:
            #I have to note that the following portion of the if statement is based on one I found in stackflow as a way to deal with integer inputs in a much better sense!
            if  gameMode == "1":
                self.mode = "A"
                try:
                    self.speed = int(input("What speed in seconds would you like for the program to run?"))
                except ValueError:
                    print("Sorry, I don't understand that...")
                else:
                    print("Press 'Q' to stop the program at any time")
                    break
            elif gameMode == "2":
                self.mode = "M"
                print("Press 'D' to move forward a generation and press 'Q' to quit the program at any time. "
                "The program will automatically end once the colony is stable.")
                break
            else:
                print("Please input a valid number.") #Add this back in when fixed

        print("You are on Generation:", generation)
        self.grid.display()        
        kbhit = KBHit()
        self.history.append(copy.deepcopy(self.grid))
        while True:
#The following will happen if the user chooses Manual Mode
            if self.mode == "M":
                if kbhit.kbhit():
                    key = kbhit.getch()
                    if key == 'd' or key == 'D':
                        self.grid.nextGeneration() #Moves to the next generation
                        self.history.append(copy.deepcopy(self.grid)) #Appends a copy to the history
                        generation+=1 #moves forward a generation
                        print("You are on Generation:", generation) #prints which generation the user is on
                        self.grid.display()
                    if len(self.history)>1:
                        stability = self.grid.generationEquality(self.history[generation-1].grid)
                        if stability == True:
                            print("Colony is stable or completely gone! Terminating simulation.")
                            return
                    if len (self.history)>2:
                        stability = True
                        stability = self.grid.generationEquality(self.history[generation-2].grid)
                        if stability == True:
                            print ("Colony is stable or completely gone! Terminating simulation.")
                            return
                    if key == 'q' or key == 'Q':
                        print("You hit quit")
                        return
#The following will take place if the user chooses automatic mode
            elif self.mode == "A":
                while True:
                    sleep(self.speed)
                    self.grid.nextGeneration()
                    self.history.append(copy.deepcopy(self.grid))
                    generation+=1
                    print("You are on Generation:", generation)
                    self.grid.display()                    
                    if kbhit.kbhit():
                        key = kbhit.getch()
                        if key == 'q' or key == 'Q':
                            print("You hit quit")
                            return
                    if len(self.history)>1:
                        stability = self.grid.generationEquality(self.history[generation-1].grid)
                        if stability == True:
                            print("Colony is stable or completely gone! Terminating simulation.")
                            return
                    if len (self.history)>2:
                        stability = self.grid.generationEquality(self.history[generation-2].grid)
                        if stability == True:
                            print ("Colony is stable or completely gone! Terminating simulation.")
                            return
