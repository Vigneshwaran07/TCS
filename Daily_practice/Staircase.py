n = int(input())
first = second = 1
tot = 0
if(n < 2):
    print(n)
for i in range(2, n+1):
    tot = first + second
    first = second
    second = tot
print(tot)
