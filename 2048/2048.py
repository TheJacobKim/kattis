#!/bin/python3

# Always go left
class Game:
    def __init__(self, board, dir):
        self.tileMatrix = board
        self.dir = dir
        self.board_size = len(self.tileMatrix)

    def move(self):
        for i in range(0, self.dir):
            self.rotateMatrixClockwise()
        if self.canMove():
            self.moveTiles()
            self.mergeTiles()

        for j in range(0, (4 - self.dir) % 4):
            self.rotateMatrixClockwise()

        for i in range(len(self.tileMatrix)):
            print(*self.tileMatrix[i])

    def rotateMatrixClockwise(self):
        tm = self.tileMatrix
        for i in range(0, int(self.board_size / 2)):
            for k in range(i, self.board_size - i - 1):
                temp1 = tm[i][k]
                temp2 = tm[self.board_size - 1 - k][i]
                temp3 = tm[self.board_size - 1 - i][self.board_size - 1 - k]
                temp4 = tm[k][self.board_size - 1 - i]
                tm[self.board_size - 1 - k][i] = temp1
                tm[self.board_size - 1 - i][self.board_size - 1 - k] = temp2
                tm[k][self.board_size - 1 - i] = temp3
                tm[i][k] = temp4

    def canMove(self):
        tm = self.tileMatrix
        for i in range(0, self.board_size):
            for j in range(1, self.board_size):
                if tm[i][j - 1] == 0 and tm[i][j] > 0:
                    return True
                elif (tm[i][j - 1] == tm[i][j]) and tm[i][j - 1] != 0:
                    return True
        return False

    def moveTiles(self):
        tm = self.tileMatrix
        for i in range(0, self.board_size):
            for j in range(0, self.board_size - 1):
                while tm[i][j] == 0 and sum(tm[i][j:]) > 0:
                    for k in range(j, self.board_size - 1):
                        tm[i][k] = tm[i][k + 1]
                    tm[i][self.board_size - 1] = 0

    def mergeTiles(self):
        tm = self.tileMatrix
        for i in range(0, self.board_size):
            for k in range(0, self.board_size - 1):
                if tm[i][k] == tm[i][k + 1] and tm[i][k] != 0:
                    tm[i][k] = tm[i][k] * 2
                    tm[i][k + 1] = 0
                    self.moveTiles()

if __name__ == '__main__':
    ar = []
    for i in range(4):
        ar.append(list(map(int, input().rstrip().split())))

    dir = int(input())
    myGame = Game(ar, dir)
    myGame.move()

