from models.constants import Shape


class Pyada:
    def __init__(self, shape: Shape):
        self.__shape = shape

    def showSymbol(self):
        return self.__shape.name

    def getShape(self):
        return self.__shape
