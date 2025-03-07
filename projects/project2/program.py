import projects.project2.__init__
from datastructures import array2d
from projects.project2.__init__ import Grid, GameController, Cell
import os

def main():
    grid = Grid(10,10)
    game_controller = GameController(grid)
    game_controller.run()

if __name__ == '__main__':
    main()
