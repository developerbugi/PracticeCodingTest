# 재귀함수의 조건을 주지않아 무한호출 되는 상황
def recursive_fuction():
    print('재귀 함수를 호출합니다.')
    recursive_fuction()

recursive_fuction()