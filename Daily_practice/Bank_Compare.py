p = int(input())
t = int(input())
ans = []
for _ in range(2):
    cost = 0
    for i in range(int(input())):
        y, r = map(float, input().split())
        cost += p*r/(1-1/((1+r)**(y*12)))
    ans.append(cost)
if(ans[0]<ans[1]):
    print("Bank A")
else:
    print("Bank B")
