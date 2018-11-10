#!/bin/python3

def myPrinter(num):
    printer = 1
    day = 1
    statues = 0
    while True:
        temp = printer * 2
        if temp > num:
            statues += printer
            if statues >= num:
                return day
            day += 1
            continue
        else:
            printer *= 2
            day += 1

if __name__ == '__main__':
    num = int(input())
    print(myPrinter(num))