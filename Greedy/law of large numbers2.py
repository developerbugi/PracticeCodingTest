"""
law of large numbers1는 M이 10000 이하이므로 M의 크기가 작을 때 해결할 수 있다
하지만 M이 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
수학적으로 접근하여 알고리즘을 해결
"""
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

count = int(m/(k+1))
count += m%(k+1)

result += first * count
result += second * (m-count)

print(result)

