# import operator
#
# def bank(myList, myTime):
#     myList.sort(key=operator.itemgetter(1))
#
#     idx = 0
#     curr = 0
#     money = 0
#     mySum = 0
#
#     while myTime >= 0 and idx < len(myList):
#         if curr != myList[idx][1]:
#             curr = myList[idx][1]
#             mySum += money
#             money = 0
#             myTime -= 1
#         money = max(money, myList[idx][0])
#         idx += 1
#
#     return mySum + money
#
# if __name__ == '__main__':
#
#     myList = []
#     inputList = list(map(int, input().rstrip().split()))
#
#     num = inputList[0]
#     myTime = inputList[1]
#
#     for i in range(num):
#         myList.append(tuple(map(int, input().rstrip().split())))
#
#     print(bank(myList, myTime))

from collections import defaultdict
from heapq import *

N, T = list(map(int, input().split()))

customers = defaultdict(list)

# read in all the customers and sort them by time
for n in range(N):
  cash, time = list(map(int, input().split()))
  customers[time].append(cash)

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