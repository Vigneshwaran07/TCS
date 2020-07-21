arr = list(map(int, input().split()))
inc = arr[0]
exc = 0
for i in range(1, len(arr)):
    temp = inc
    inc = max(inc, exc+arr[i])
    exc = temp
print(max(inc, exc))
