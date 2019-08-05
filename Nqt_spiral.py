n = int(input())

mod = n%4
div = (n//4)+1

if(n%4==0 and n>4):
    div = n//4

if(n<=4):
    div = 1

x, y = 20, 20

if(mod == 0):
    print(-20*div, -20*div)
elif(mod == 1):
    print((20*div)-10, -20*(div-1))
elif(mod == 2):
    print((20*div)-10,20*div)
elif(mod == 3):
    print(-20*div, 20*div)
