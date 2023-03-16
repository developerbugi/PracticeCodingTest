"""
파이썬의 장점을 살린 퀵 정렬 소스코드
전통 퀵 정렬의 분할 방식보다 비교 연산 횟수가 증가하여 시간 면에서 조금 비효율적이다.
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 정렬된 left_side, pivot, right_side 를 합쳐서 반환
    return sort(left_side) + [pivot] + sort(right_side)

print(sort(array))

