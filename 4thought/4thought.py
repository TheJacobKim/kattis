#!/bin/python3
from itertools import combinations_with_replacement

if __name__ == '__main__':
    # Build combinations
    lst = [" + 4", " - 4", " * 4", " / 4"]
    comb = combinations_with_replacement(lst, 3)

    ans = []
    for item in comb:
        ans.append("4" + ''.join(list(item)))

    # Input
    ar = []
    num = int(input())
    for i in range(num):
        ar.append(int(input()))

    # Find solution
    for val in ar:
        for item in ans:
            sol = False
            if eval(item) == val:
                sol = True
                print(item + " = " + str(val))
                break

        if not sol:
            print("no solution")