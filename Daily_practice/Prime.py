def isprime(n):
    if(n<=1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
prime = []

n = int(input())
for i in range(2,n+1):
    flag = 0
    for j in range(2, (n//2)+1):
        if(i%j==0):
            flag = 1
    if(flag==0):
        prime.append(i)
tot = 0
ans = 0
for i in prime:
    tot += i
    if isprime(tot):
        ans += 1
print(ans)
