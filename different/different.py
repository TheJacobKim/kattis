#!/bin/python3

if __name__ == '__main__':
    contents = []
    while True:
        try:
            line = list(map(float, input().rstrip().split()))
        except EOFError:
            break
        contents.append(line)

    for item in contents:
        print(format(round(abs(item[0]-item[1]), 1), '.0f'))
