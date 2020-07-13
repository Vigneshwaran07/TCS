for _ in range(int(input())):
    n = int(input())
    ans = (2**(n//2 + 1))-1
    if(n%2==0):
        print(ans)
    else:
        print(ans*2)
