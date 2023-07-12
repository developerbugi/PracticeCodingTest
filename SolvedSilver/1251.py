"""
s = 'mobitel'

x = ''.join(sorted(s))

print(x)
"""
s = input()

min = 'z' * 50

for i in range(0,len(s)-2):
    for j in range(i+1,len(s)-1):
        s1 = s[:i+1]
        s2 = s[i+1:j+1]
        s3 = s[j+1:]
        s1 = s1[::-1]
        s2 = s2[::-1]
        s3 = s3[::-1]
        s4 = s1 + s2 + s3
        if min >= s4:
            min = s4
        else:
            continue

print(min)