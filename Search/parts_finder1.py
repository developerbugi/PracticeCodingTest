"""
동빈이네 전자매장에는 부품이 N개 있다.
각 부품은 정수 형태의 고유한 번호가 있다.
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하라.
"""

n = int(input())

parts = list(map(int, input().split()))

m = int(input())

request_parts = list(map(int, input().split()))

result = [0] * len(request_parts)


for i in range(m):
    for j in range(n):
        if request_parts[i] == parts[j]:
            result[i] = 1
            parts[j] = -1 #부품에 수량이 정해져있다고 생각하고 부품의 갯수를 생각해본 코드
            break

for i in range(len(result)):
    if result[i] == 1:
        result[i] = 'yes'
    else:
        result[i] = 'no'

print(result)
