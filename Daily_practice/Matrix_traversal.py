from math import factorial
m, n = map(int, input().split())
a = factorial(m+n-2)
b = factorial(n-1) * factorial(m-1)
print(a//b)
