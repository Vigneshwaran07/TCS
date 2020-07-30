n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
score = 0
happy = sum([1 for i in arr if i in A])
sad = sum([1 for i in arr if i in B])
print(happy-sad)
