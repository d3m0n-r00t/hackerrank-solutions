def almostSorted(arr):
    brr = arr.copy()
    brr.sort()
    fl = 0
    subarr = []
    for_swap = []
    if (arr == brr):
        print('yes')
        exit(0)
    for i in range(len(arr)):
        if arr[i] != brr[i]:
            for_swap.append(i+1)
            subarr.append(arr[i])
    if len(for_swap) == 2:
        print("yes")
        print("swap {} {}".format(for_swap[0], for_swap[1]))
        exit(0)
    else:
        if subarr == sorted(subarr)[::-1]:
            print("yes")
            print("reverse {} {}".format(arr.index(subarr[0])+1, arr.index(subarr[-1:][0])+1))
            exit(0)
        else:
            print("no")
            exit(0)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)