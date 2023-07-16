a, b, n = map(int, input().split())

arr = []

for _ in range(n):
    a = (a - (a//b) * b) * 10
    arr.append(a//b)

print(arr[n-1])