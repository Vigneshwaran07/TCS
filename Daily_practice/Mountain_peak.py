n = int(input())
ans = 2
if(n > 2):
    if(n == 3):
        print(ans)
    else:
        for i in range(n-3):
            ans = (ans*2)+2
        print(ans)
else:
    print(0)
