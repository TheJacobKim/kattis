#!/bin/python3

if __name__ == '__main__':
    ### input handling ###
    num = list(map(int, input().rstrip().split()))

    jack = set()
    jill = set()
    for i in range(num[0]):
        jack.add(int(input()))

    ans = 0
    for j in range(num[1]):
        if int(input()) in jack:
         ans += 1

    print(ans)
