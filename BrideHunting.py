m, n = map(int, input().split())
a = [[0] * n for i in range(m)]
res = [[0] * n for i in range(m)] #result matrix intialization
for i in range(m):
    a[i] = list(map(int, input().split()))
ans = []
maxi = 0
a[0][0] = 0
count = 0
'''Consider a matrix
1 2 3
4 5 6
7 8 9
'''
for i in range(m):
    for j in range(n):
        if (a[i][j] == 1):
            if (i == 0 and j == 0):#SAM place, so no manipulation
                continue
            if (i == 0 and j != n - 1):#find qualities at 2
                count = a[i][j - 1] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j - 1] + a[i + 1][j + 1]
            elif (i == 0 and j == n - 1):#find qualities at 3
                count = a[i][j - 1] + a[i + 1][j - 1] + a[i + 1][j]
            elif (i == m - 1 and j == 0):#find qualities at 7
                count = a[i - 1][j] + a[i - 1][j + 1] + a[i][j + 1]
            elif (i == m - 1 and j != n - 1):#find qualities at 8
                count = a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j - 1] + a[i][j + 1]
            elif (i == m - 1 and j == n - 1):#find qualities at 9
                count = a[i - 1][j] + a[i - 1][j - 1] + a[i][j - 1]
            elif (i != 0 and i != m - 1 and j == 0):#find qualities at 4
                count = a[i - 1][j] + a[i - 1][j + 1] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
            elif (i != 0 and i != m - 1 and j == n - 1):#find qualities at 6
                count = a[i - 1][j] + a[i - 1][j - 1] + a[i][j - 1] + a[i + 1][j - 1] + a[i + 1][j]
            else:#find qualities at 6
                count = a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j - 1] + a[i][j + 1] + a[i + 1][j - 1] + \
                        a[i + 1][j] + a[i + 1][j + 1]
            #find qualities at 'i' represents above example matrix, it denotes position
            if (count > maxi):
                maxi = count
                ans = [] #empty ans list everytime when you got new maximum
                ans.append([i + 1, j + 1, count]) #and add new maximum in ans list in i,j,conunt format
            elif count == maxi:#already
                ans.append([i + 1, j + 1, count])#if more maxi found just add in ans list
            res[i][j] = count
if (len(ans) == 0):
    print("No suitable girl found")
else:
    ans = sorted(ans, key=lambda a: a[0] * a[1]) # sort by i*j(multiply), to find distance
    if (len(ans) > 1): #if more than 1 maximum found
        if (ans[0][0] * ans[0][1] == ans[1][0] * ans[1][1]):#with same distance
            print("Polygamy not allowed")
        else:
            print("{}:{}:{}".format(*ans[0]))
    else:
        print("{}:{}:{}".format(*ans[0]))

# print(*res, sep="\n")
# print(*ans, sep="\n")
