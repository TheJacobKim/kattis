#!/bin/python3

import os
import sys

if __name__ == '__main__':
    smallest = int(input())
    ar = list(map(float, input().rstrip().split()))

    a1 = 1/2
    for i in range(2, smallest+1):
        a1 =- 1/pow(2, i)


