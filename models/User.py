from models.Pyada import Pyada


class User:
    def __init__(self, name: str, pyada: Pyada):
        self.__name = name
        self.__pyada = pyada

    def getName(self) -> str:
        return self.__name

    def getPyada(self) -> Pyada:
        return self.__pyada
