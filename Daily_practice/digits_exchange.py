from itertools import permutations
a, b = input().split()
if(len(a) < len(b)): #99 100
    print(-1)
elif(len(a) > len(b) and a.count('0')==0): #971 77, 205 27
    print(''.join(sorted(a)).lstrip('0'))
else:
    flag = 0
    ans = 0
    for i in permutations(sorted(a)):
        if(int(''.join(i))>int(b)):
            flag = 1
            ans = int(''.join(i))
            break
print(ans if flag==1 else -1)
