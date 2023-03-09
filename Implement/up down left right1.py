"""
여행가 A는 N X N 크기의 정사각형 공간위에 서있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
가짱 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상(1,1)이다.

L -> 왼쪽으로 한칸 이동
R -> 오른쪽으로 한칸 이동
U -> 위로 한칸 이동
D -> 밑으로 한칸 이동

이때 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
"""

n = int(input())

move = input().split()

x = 1
y = 1

for i in move:
    if i=='L' and y>1:
        y -= 1
    elif i=='R' and y<n:
        y += 1
    elif i=='U' and x>1:
        x -= 1
    elif i=='D' and x<n:
        x += 1
    else:
        continue

print(x, y)



