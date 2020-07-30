n = int(input())
p = 0
l = list(range(1, n*(n+1)+1))
rev = l[::-1]
s = " "
start = 0
for end in range(n,0,-1):
    print(s*p,end="")
    print(*l[start:start+end],*rev[start:start+end][::-1],sep="*")
    start += end
    p += 2
