from models.Pyada import Pyada
from models.constants import Shape
from exceptions.InvalidMove import InvalidMove


class Grid:
    def __init__(self, size):
        self.__grid = [[None] * 3 for i in range(size)]

    def getGrid(self) -> list:
        return self.__grid

    def getValue(self, row: int, col: int) -> Pyada:
        return self.__grid[row][col]

    def setValue(self, row: int, col: int, shape: Shape):
        if row >= len(self.__grid) or col >= len(self.__grid) or self.getValue(row, col):
            raise InvalidMove(row, col)
        self.__grid[row][col] = shape
        return True
