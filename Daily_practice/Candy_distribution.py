for _ in range(int(input())):
    p,m,s = map(int, input().split())
    a=0
    a=(m+s-1)%p
    if a==0:
        print(p) 
    else:
        print(a)
