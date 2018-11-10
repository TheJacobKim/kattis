#!/bin/python3

import os
import sys

def aboveaverage(ar):

    for myTup in ar:
        num = myTup[0]
        sum = 0
        for i in range(1, len(myTup)):
            sum += myTup[i]
        avg = sum/num

        count = 0
        for i in range(1, len(myTup)):
            if(myTup[i] > avg):
                count+=1

        print(format(round((count/num)*100, 3), '.3f') + "%")

if __name__ == '__main__':
    ar = []
    ar_count = int(input())
    for i in range(ar_count):
        ar.append(tuple(map(float, input().rstrip().split())))

    aboveaverage(ar)

