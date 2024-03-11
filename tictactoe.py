from models.Grid import Grid
from models.User import User
from models.UserFactory import UserFactory
from models.constants import WinStatus, Shape
from collections import deque

from service.TictactoeService import checkGameStatus, move, showBoardPretty

SIZE = 3


class Tictactoe:
    def __init__(self):
        self.__player2: User = None
        self.__player1: User = None
        self.__board: Grid = Grid(SIZE)
        self.__winStatus = WinStatus.UNDECIDED
        self.__players: deque = deque()

    def initialize(self):
        uname1 = input("Enter Name of Player 1: ")
        uname2 = input("Enter Name of Player 2: ")
        userFactory = UserFactory()
        self.__player1: User = userFactory.getUser(uname1, Shape.X)
        self.__player2: User = userFactory.getUser(uname2, Shape.O)
        self.__players.append(self.__player1)
        self.__players.append(self.__player2)

    def play(self):
        #printing board at the start
        showBoardPretty(self.__board)

        #printing symbol of both player
        print(self.__player1.getName(), "'s Symbol: ", self.__player1.getPyada().showSymbol())
        print(self.__player2.getName(), "'s Symbol: ", self.__player2.getPyada().showSymbol())

        while self.__winStatus == WinStatus.UNDECIDED:
            activePlayer: User = self.__players.popleft()
            self.__players.append(activePlayer)
            print("\nPlayer {} turn".format(activePlayer.getName()))
            move(self.__board, activePlayer)
            showBoardPretty(self.__board)
            self.__winStatus, winner = checkGameStatus(self.__board)
            if self.__winStatus == WinStatus.DRAW:
                print("Match is a Draw")
            elif self.__winStatus == WinStatus.WON:
                print("\nPlayer {} is the winner".format(activePlayer.getName()))
