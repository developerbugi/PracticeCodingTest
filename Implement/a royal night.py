"""
왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다.
나이트는 정원 밖으로 나갈 수 없으며 다음과 같이 움직인다.
1. 수평으로 두칸 이동한 뒤에 수직으로 한칸 이동하기
2. 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동하
"""

location = input()

row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1
result = 0

move_type = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]


for move in move_type:
    next_row = row + move[0]
    next_column = column + move[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
