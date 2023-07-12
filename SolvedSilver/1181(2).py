import sys

n = int(sys.stdin.readline().strip())

# 중복된 원소를 제거하기 위해 set 자료형 사용
arr = set()

for _ in range(n):
    arr.add(sys.stdin.readline().strip())

arr2 = list(arr)
arr3 = []

for a in arr2:
    arr3.append(len(a))

dic = dict(zip(arr2,arr3))

dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))

for i in range(len(dic)):
    print(dic[i][0])

