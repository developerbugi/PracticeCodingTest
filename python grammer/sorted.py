
# sorted 함수, 기본값 : 오름차순 정렬을
result = sorted([9, 1, 8, 5, 4])
print(result)

# reverse 옵션을 사용하여 내림차순 정렬
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

# key 속성을 이용한 정렬 기준 선택
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x : x[1])
print(result)