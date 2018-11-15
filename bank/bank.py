
from collections import defaultdict
from heapq import *

if __name__ == '__main__':
    num, T = list(map(int, input().split()))

    customers = defaultdict(list)

    # read in all the customers and sort them by time
    for i in range(num):
        money, time = list(map(int, input().split()))
        customers[time].append(money)

    amounts_to_consider = []
    sum_total = 0

    # greedy solution:
    # start looking at customers who will stay the longest time
    # then move to those who will stay the shortest time
    for t in range(T)[::-1]:
        # add all the amounts of current customers to a max heap
        for price in customers[t]:
            # negating price since heapq is min heap by default
            # so we make the "max" value into the most negative
            heappush(amounts_to_consider, -price)
        # if there are customers who will wait at least time t,
        # pop the max amount from those customers
        if amounts_to_consider:
            sum_total += heappop(amounts_to_consider)

    # negate the negation
    print(-sum_total)
