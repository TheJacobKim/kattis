#!/bin/python3

def abc(ar, myStr):
    big = myStr.index('C')
    mid = myStr.index('B')
    small = myStr.index('A')

    ar.sort()

    ans = [0, 0, 0]

    ans[small] = ar[0]
    ans[mid] = ar[1]
    ans[big] = ar[2]

    for i in ans:
        print(i, end=" ")


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    myStr = str(input())

    abc(ar, myStr)