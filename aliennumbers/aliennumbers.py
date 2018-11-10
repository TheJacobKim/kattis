#!/bin/python3

import os
import sys

def alienNumbers(ar):
    caseNum = 1
    for case in ar:
        # source language interpretation
        currBase = len(case[1])
        digit = 1
        sum = 0
        for i in range(len(case[0]) - 1, -1, -1):
            sum += case[1].index(case[0][i]) * digit
            digit *= currBase

        # target language interpretation
        targetBase = len(case[2])
        digit = 1
        ans = ""
        while sum > 0:
            rem = sum % targetBase
            ans += case[2][rem]
            sum //= targetBase

        print("Case #" + str(caseNum) + ": " + ans[::-1])
        caseNum+=1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar = []
    ar_count = int(input())
    for i in range(ar_count):
        ar.append(list(input().rstrip().split()))

    alienNumbers(ar)
