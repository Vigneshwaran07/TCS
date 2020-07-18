for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    time = 0
    while(len(arr)>2):
        aMin = min(arr)
        del arr[arr.index(aMin)]
        bMin = min(arr)
        del arr[arr.index(bMin)]
        time += aMin + bMin
        arr.append(aMin+bMin)
    print(time + sum(arr))
