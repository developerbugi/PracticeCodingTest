n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if b[i] > a[i]:
        b[i], a[i] = a[i], b[i]

result = 0

for i in a:
    result += i

print(result)