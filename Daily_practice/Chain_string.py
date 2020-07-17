for _ in range(int(input())):
    n = int(input())
    arr = input().lower().split()
    if(all(arr[i-1][-1] == arr[i][0] for i in range(n))):
        print(1)
    else:
        print(0)
