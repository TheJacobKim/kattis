#!/bin/python3

import os
import sys

def qaly(ar):
    sum = 0
    for myTup in ar:
        sum += myTup[0]*myTup[1]

    return sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar = []
    ar_count = int(input())
    for i in range(ar_count):
        ar.append( tuple(map(float, input().rstrip().split())) )

    result = qaly(ar)

    print(result)
