"""
N가지 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서가 다른 것은 같은 경우로 구분한다.
"""

n, m = map(int,input().split())

dollar = []

for i in range(n):
    dollar.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(dollar[i], m+1):
        if d[j-dollar[i]] != 10001:
            d[j] = min(d[j], d[j-dollar[i]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])





