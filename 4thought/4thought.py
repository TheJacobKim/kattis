#!/bin/python3

import operator


def thought(val):
    ops = {0: operator.add,
           1: operator.sub,
           2: operator.mul,
           3: operator.truediv}

    opsArr = ["+", "-", "*", "/"]

    for i in range(0, 4):
        op1 = ops[i]
        for j in range(0, 4):
            op2 = ops[j]
            for k in range(0, 4):
                op3 = ops[k]
                try:
                    ans = op1(op2(op3(4, 4), 4), 4)
                except ZeroDivisionError:
                    continue
                if ans == val:
                    print("4 " + opsArr[i] + " 4 " + opsArr[j] + " 4 " + opsArr[k] + " 4 = " + str(val))
                    return
    print("no solution")

if __name__ == '__main__':
    ar = []
    num = int(input())
    for i in range(num):
        ar.append(int(input()))

    for val in ar:
        thought(val)