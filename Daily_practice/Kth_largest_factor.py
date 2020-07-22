n, k = map(int, input().split())
arr = [i for i in range(1, n+1) if(n%i == 0)]
print('-1' if k>len(arr) else arr[-k])
