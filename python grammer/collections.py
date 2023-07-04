from collections import deque

data = deque([2, 3, 4])

# 가장 왼쪽에 삽입 , pop도 동일하게 작용
data.appendleft(1)

# 가장 오른쪽에 삽입, pop도 동일하게 작용
data.append(5)

print(data)


from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

# blue가 등장한 횟수 출력
print(counter['blue'])

# 사전 자료형으로 변경하는 법
print(dict(counter))

