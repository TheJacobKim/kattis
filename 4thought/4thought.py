#!/bin/python3
from itertools import product

if __name__ == '__main__':
    # Build product
    lst = [" * 4", " // 4", " + 4", " - 4"]
    comb = product(lst, repeat=3)

    myDict = {}
    for item in comb:
        equation = str("4" + ''.join(list(item)))
        myDict[eval(equation)] = equation.replace("//", "/")

    # Input
    num = int(input())
    for i in range(num):
        val = int(input())
        if val in myDict:
            print(myDict[val] + " = " + str(val))
        else:
            print("no solution")
