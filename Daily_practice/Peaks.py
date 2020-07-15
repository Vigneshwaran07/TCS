n = int(input())
a = list(map(int, input().split()))
peaks=[]
for i in range(n):
    if(i==0):
        if(a[i]>a[i+1]):
            peaks.append(i)
    elif(i==n-1):
        if(a[i]>a[i-1]):
            peaks.append(i)
    elif(a[i-1]<a[i] and a[i]>a[i+1]):
        peaks.append(i)
diff = [abs(peaks[i]-peaks[i+1]) for i in range(len(peaks)-1)]
print(max(diff))
