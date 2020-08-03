n = int(input())
arr = [1]
print(*arr)
for i in range(n-2):
    arr.append(arr[-1]*2)
    print(*arr,*arr[:-1][::-1])
