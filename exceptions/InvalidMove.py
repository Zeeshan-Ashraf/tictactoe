class InvalidMove(Exception):
    def __init__(self,row,col):
        print("Invalid move for row,col",row,col)