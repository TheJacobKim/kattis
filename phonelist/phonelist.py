#!/bin/python3
class Node:
    left = None
    middle = None
    right = None
    flag = False
    def __init__(self, char):
        self.char = char

def insert(node, string):
    while len(string) >= 0:
        head = string[0]

        # if head < node.char:
        #     node.left = Node(head)
        #     node = node.left
        # elif head > node.char:
        #     node.right = Node(head)
        # else:
        #     if len(tail) == 0


    if len(string) == 0:
        return node

    head = string[0]
    tail = string[1:]
    if node is None:
        node = Node(head)

    if node.flag:
        print("NO")
        return None

    if head < node.char:
        node.left = insert(node.left, string)
    elif head > node.char:
        node.right = insert(node.right, string)
    else:
        if len(tail) == 0:
            node.flag = True
        else:
            node.middle = insert(node.middle, tail)

    return node

class TST:
    # a simple wrapper
    root = None
    def __init__(self, string):
        self.append(string)
    def append(self, string):
        self.root = insert(self.root, string)

if __name__ == '__main__':
    ### input handling ###
    tests = int(input())
    for i in range(tests):
        cases = int(input())
        tst = TST(input())
        for j in range(cases-1):
            TST.append(input())

