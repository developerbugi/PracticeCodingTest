"""
1. 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용
2. 총 시간 복잡도 O(N³)
3. 점화식 -> D𝑎𝖻 = min(D𝑎𝖻, D𝑎k + Dk𝖻)
"""

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

#각 간선에 대한 정보 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for b in range(1, n+1):
        for a in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()

