"""
263p 최단경로 전보문제
"""

import heapq
import sys

# 반복문으로 여러줄을 입력받아야 할 상황에 input()으로 입력 받는다면 시간 초과가 발생할 수 있다.
input = sys.stdin.readline

INF = int(1e9)

# n = 도시의 갯수, 통로의 갯수 m, 메시지를 보내고자 하는 도시 c
n, m, start = map(int, input().split())

# 그래프 입력
graph = [[] for _ in range(n+1)]

# 거리
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 메시지를 받을 수 있는 도시의 총 개수를 저장하기 위한 변수
count = 0

#총 걸리는 시간을 저장하기 위한 변수
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)






