"""
반복문으로 구현한 이진탐색
"""

def binary_search(arary, target, start, end):
    while start <= end:

        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif arary[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        return None

n, target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("찾으려는 원소가 존재하지 않습니다.")
else:
    print(result + 1)