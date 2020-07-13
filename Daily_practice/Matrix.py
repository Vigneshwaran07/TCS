n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
left = 0
right = 0
for i in range(n):
    for j in range(n):
        if(i==j):
            left += matrix[i][j]
        if(i+j == n-1):
            right += matrix[i][j]
print(abs(left-right))
