"""
N개의 배열이 있을 때 동빈이의 큰수의 법칙은 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 도빈이의 큰 수의 법칙에 따른 결과를 출력해라.

입력조건 : 1. 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
        2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000 이하의 수로 주어진다.
        3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0
count = 0

for i in range(m):
    if count>=k:
        count=0
        result += second
    else:
        result+=first
        count+=1

print(result)


