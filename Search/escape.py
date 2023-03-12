"""
동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다.
미로에는 여러마리의 괴물이 존재하고 이를 피해 탈출해야한다.
동빈이의 위치는(1,1)이고 미로의 출구는(N,M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0, 없는 부분은 1로 표시된다.
동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오
"""

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))



