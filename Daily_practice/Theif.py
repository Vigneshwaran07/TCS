arr = list(map(int, input().split()))
now = arr[0]
prev = 0
for i in range(1, len(arr)):
    temp = now
    now = max(now, prev+arr[i])
    prev = temp
print(max(now, prev))
