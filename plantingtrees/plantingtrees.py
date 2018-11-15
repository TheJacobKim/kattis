if __name__ == '__main__':
    num = input()

    # read in all the seedlings and sort them
    seedlings = list(map(int, input().split()))
    seedlings.sort(reverse=True)

    daysLeft = seedlings[0]
    count = 1
    idx = 1
    while daysLeft >= 0:
        if idx < len(seedlings) and daysLeft < seedlings[idx]:
            daysLeft += seedlings[idx] - daysLeft
        idx += 1
        daysLeft -= 1
        count += 1

    print(count)