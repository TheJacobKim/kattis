#!/bin/python3

import os
import sys

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar = []
    x = int(input())
    y = int(input())

    if( x > 0 and y > 0 ):
        print(1)
    elif( x > 0 and y < 0 ):
        print(4)
    elif( x < 0 and y > 0 ):
        print(2)
    else:
        print(3)
