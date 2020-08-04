n,t = map(int, input().split())
a = list(map(int, input().split()))
for i in range(t):
    x,y = map(int, input().split())
    print(min(a[x:y+1]))
