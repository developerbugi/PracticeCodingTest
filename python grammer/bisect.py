from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 특정 범위에 속하는 원소의 개수를 구할 때
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    return right_index - left_index

b = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4개인 데이터 개수 찾기
print(count_by_range(b, 4, 4))

# -1 부터 3 까지 범위에 있는 데이터 개수 찾기
print(count_by_range(b, -1, 3))

