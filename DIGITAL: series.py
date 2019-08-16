n = int(input())
tot = 0
for ind,i in enumerate(bin(n)[2:][::-1]):
    tot += int(i)*(4**ind)
print(tot)


#1 4 5 16 17 20 21 64 65
