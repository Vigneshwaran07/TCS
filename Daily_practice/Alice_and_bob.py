
for _ in range(int(input())):
    n = int(input())
    if(n%4!=1):
        print("Female")
    else:
        print("Male")
        
'''
#General approch for solving these types of problems
for _ in range(int(input())):
    n = int(input())
    dp = [0]*(n+1)
    
    dp[0] = True
    dp[1] = False
    dp[2] = True
    dp[3] = True
    
    for i in range(4, n+1):
        dp[i] = not(dp[i-1] and dp[i-2] and dp[i-3])
    print("Female" if dp[n-1] else "Male" )
'''    
