num = int(input())
tot = ""
while(num!=0):
    tot += str(num%4)
    num //= 4
try:
    n = int(tot[::-1],2)
    print("Yes")
    print(n)
except:
    print("No")
    
    #check Digital:series


#Logic2
num = int(input())
tot = bin(num)[2:]
if(len(tot)%2!=0 and all(tot[i]=='0' for i in range(1,len(tot),2))):
    for i in range(1,len(tot),2):
        tot = list(tot)
        tot[i] = '-'
    tot = ''.join(''.join(tot).split('-'))
    print("Yes",int(tot,2))
else:
    print("NO")
