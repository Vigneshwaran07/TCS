def check(s, res):
    if(len(res) > len(s)): #what if no of rotation is 40, ur string len is 5
        return False
    else:
        for i in range(0,len(s)-len(res)+1):
            if(sorted(s[i:i+len(res)]) == res):
                return True
        return False
s = input()
res = ""
index = 0
for _ in range(int(input())):
    side, mag = input().split()
    if(side == 'L'):
        index = (index + int(mag))%len(s)
    elif(side == 'R'):
        index = (index - int(mag))%len(s)
    res += s[index]
    
res = sorted(res)
print("YES" if(check(s, res)) else "NO")
