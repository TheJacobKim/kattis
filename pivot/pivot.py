import copy

def findPivot(ar, num):
    unsortedAr = copy.deepcopy(ar)
    ar.sort()
    ans = 0
    for i in range(num):
        if unsortedAr[i] == ar[i]:
            pivot = ar[i]
            isPivot = True
            for j in range(0, num):
                if j != i and not( (j < i and unsortedAr[j] < pivot) or (j > i and unsortedAr[j] > pivot) ) :
                    isPivot = False
                    break
            if isPivot:
                ans += 1
    return ans

if __name__ == '__main__':
    num = int(input())
    ar = list(map(int, input().rstrip().split()))


    print(findPivot(ar,num))





