n = int(input())

d = [0] * int((n/2))

d[0] = 6


for i in range(2,int(n/2)):
    d[i] = d[i-1]*3

print(d[len(d)-1])