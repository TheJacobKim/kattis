
def convert_to_hex(binary):
    num = int(binary, 2)
    return "%X" % num

if __name__ == '__main__':
    val = int(input(), 8)
    print('{0:x}'.format(val).upper())

    # # Input
    # numList = list(input())
    #
    # count = 0
    # binaryList = []
    # for item in numList:
    #     binaryList += list('{0:03b}'.format(int(item)))
    #
    # print(binaryList)
    # count = 0
    # temp = ''
    # ans = ''
    # for binary in reversed(binaryList):
    #     if count == 4:
    #         ans = convert_to_hex(temp) + ans
    #         temp = binary
    #         count = 1
    #     else:
    #         temp = binary + temp
    #         count += 1
    # ans = convert_to_hex(temp) + ans
    # print(ans.lstrip("0"))
