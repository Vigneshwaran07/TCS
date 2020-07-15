for _ in range(int(input())):
    p = input()
    s = input()
    ans = ""
    for i in p:
        if i in s:
            ans += i*s.count(i)
    print(ans)
