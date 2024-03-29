import sys
input = sys.stdin.readline

INF = int(1e9)

#노드의 개수 = n , 간선의 개수 = m
n, m = map(int, input().split())

#시작 노드 입력 = start
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for i in range(n+1)]

#방문 여부를 판단하기 위한 리스트
visted = [False] * (n+1)

#거리 모두 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if visted[i] == False and min_value > distance[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드 초기화
    distance[start] = 0
    visted[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    #시작 노드를 제외한 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visted[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINTIY")
    else:
        print(distance[i])


