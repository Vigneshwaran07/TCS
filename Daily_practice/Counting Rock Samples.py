s, r = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(r):
    x, y = map(int, input().split())
    count = sum([1 for i in arr if i>=x and i<=y])
    print(count, end=" ")
