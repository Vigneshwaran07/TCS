from itertools import combinations

n = int(input())
s = input()
unique = set(s)
delCount = len(unique) - 2
ans = 0
if(len(unique) > 1):
    for i in combinations(unique, delCount):
        temp = s
        count = 0
        for j in i:
            temp = temp.replace(j, '')
        if(all(temp[k]!=temp[k+1] for k in range(len(temp)-1))):
            if(ans < len(temp)):
                ans = len(temp)
    print(ans)
else:
    print(ans)
