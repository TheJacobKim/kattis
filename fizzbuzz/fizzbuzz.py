if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))

    for i in range(1, ar[2]+1):
        str = ""
        if i%ar[0] == 0:
            str += "Fizz"
        if i%ar[1] == 0:
            str += "Buzz"
        if str == "":
            print(i)
        else:
            print(str)
