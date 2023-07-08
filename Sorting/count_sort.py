"""
계수 정렬은 특정한 조건이 부합할 때만 사용할 수 있는 매우 빠른 정렬 알고리즘
1. 데이터의 크기 범위가 제한 되어 정수 형태로 표현할 수 있을 때
2. 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (len(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")


