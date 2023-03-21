"""
이진 탐색을 이용한 탐색 문제 풀이
"""

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())

parts = list(map(int, input().split()))

parts.sort()

m = int(input())

request_parts = list(map(int, input().split()))

for i in request_parts:
    result = binary_search(parts, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')