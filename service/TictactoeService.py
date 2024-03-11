from models.Grid import Grid
from models.User import User
from models.constants import WIN_CORD, WinStatus


def move(grid: Grid, player: User):
    while True:
        try:
            (row, col) = input("Enter Row Col: ").split()
            grid.setValue(int(row), int(col), player.getPyada().getShape())
        except Exception as e:
            print(e, "\nPlz try again {}".format(player.getName()))
        else:
            break


def showBoardPretty(board: Grid):
    for row in board.getGrid():
        print("|", end='')
        for item in row:
            if item is not None:
                print(item.value + "|", end='')
            else:
                print(" |", end='')
        print("")


def checkGameStatus(grid: Grid):
    playerPosition = {}
    for row in range(len(grid.getGrid())):
        for col in range(len(grid.getGrid())):
            item = grid.getGrid()[row][col]
            if item not in playerPosition:
                playerPosition[item] = {(row, col)}
            else:
                playerPosition[item].add((row, col))

    winner = None
    for k, v in playerPosition.items():
        if k is not None:
            for cords in WIN_CORD:
                if (cords & v) in WIN_CORD:
                    winner = k
                    break
        if winner is not None:
            break

    if None not in playerPosition and winner is None:
        return WinStatus.DRAW, None
    elif winner is None:
        return WinStatus.UNDECIDED, None
    return WinStatus.WON, winner
