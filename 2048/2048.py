#!/bin/python3
import numpy as np

def rotate(ar, degree):
    if degree == 0:
        return ar
    elif degree > 0:
        return rotate(list(zip(*ar[::-1])), degree-90)
    else:
        return rotate(list(zip(*ar)[::-1]), degree+90)

def playGame(ar, move):
    rotateDegree = [0, 270, 180, 90]
    myList = list(rotate(ar, rotateDegree[move]))

    # # Move left
    for row in myList:
        i = 1
        while i < 4:
            # If 0 move
            if row[i-1] == 0:
                row[i-1] = row[i]
                if i < 3:
                    row[i] = row[i + 1]
                    row[i+1] == 0
                else:
                    row[i] = 0

                #continue

            # If same, double
            if row[i] == row[i-1]:
                row[i-1] *= 2
                row[i] = 0
                #continue

            i += 1
    print(myList)

if __name__ == '__main__':
    ar = []
    for i in range(4):
        ar.append(list(map(int, input().rstrip().split())))

    move = int(input())
    playGame(ar, move)

