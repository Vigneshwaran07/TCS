from math import gcd

def lcm(a, b):
    return((a*b)//gcd(a,b))

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    turn = 1
    cturn = 0
    pos = 0
    for i in range(n):
        cturn = 0
        pos = i
        while(arr[pos]!=0):
            temp = pos
            pos = arr[pos]-1
            arr[temp] = 0
            cturn += 1
        if(cturn != 0):
            turn = lcm(turn, cturn)
    print(turn)
