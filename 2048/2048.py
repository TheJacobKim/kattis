#!/bin/python3

def playGame(ar, move):
    # Move left
    if move == 0:
        for row in ar:

            # First deal with zeros
            i = 1
            while i < 4:
                # If same, double
                if row[i-1] == row[i]:
                    row[i-1] *= 2
                    row[i] = 0
                    continue

                # If 0 move
                if row[i-1] == 0:
                    row[i] = row[i+1]
                    row[i+1] == 0

                i += 1

    print(ar)

if __name__ == '__main__':
    ar = []
    for i in range(4):
        ar.append(list(map(int,input().rstrip().split())))

    move = int(input())
    playGame(ar, move)

