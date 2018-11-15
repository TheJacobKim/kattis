def checkQueen(myList, i, j):
    # Check horizontal and vertical
    for idx in range(8):
        if idx != j and myList[i][idx] == '*':
            return False

        if idx != i and myList[idx][j] == '*':
            return False

    # Check top left to bottom right
    a = i
    b = j
    while a > 0 and b > 0:
        a -= 1
        b -= 1

    while a < 8 and b < 8:
        if (a != i and b != j) and myList[a][b] == '*':
            return False
        a += 1
        b += 1

    # Check top right to bottom left
    a = i
    b = j
    while a > 0 and b < 7:
        a -= 1
        b += 1

    while a < 8 and b >= 0:
        if (a != i and b != j) and myList[a][b] == '*':
            return False
        a += 1
        b -= 1

    return True


def eightQueen(myList):
    check = 0
    correct = True
    for i in range(8):
        for j in range(8):
            if myList[i][j] == '*':
                check += 1
                if not checkQueen(myList, i, j):
                    correct = False
    if check != 8:
        return False

    return correct

if __name__ == '__main__':

    myList = []
    for i in range(8):
        myList.append(list(input()))

    if eightQueen(myList):
        print("valid")
    else:
        print("invalid")