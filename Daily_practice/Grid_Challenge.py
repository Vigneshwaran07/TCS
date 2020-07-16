for _ in range(int(input())):
    n = int(input())
    matrix = []
    flag = 0
    for i in range(n):
        matrix.append(sorted(list(input())))
    for i in zip(*matrix):
        if(list(i) != sorted(list(i))):
            flag = 1
            break
    print("YES" if flag==0 else "NO")
    
'''
1
5
eabcd
fghij
olkmn
trpqs
xywuv
'''
