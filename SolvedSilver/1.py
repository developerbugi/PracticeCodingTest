import heapq

n = int(input())

meets = []  # 회의
for x in range(n) :
  start, end = map(int, input().split())
  meets.append([start, end])

meets.sort()

meets_rooms = []
heapq.heappush(meets_rooms, meets[0][1])

for i in range(1,n):
  if meets[i][0] < meets_rooms[0] :
    heapq.heappush(meets_rooms, meets[i][1])
  else:
    heapq.heappop(meets_rooms)
    heapq.heappush(meets_rooms, meets[i][1])

print(len(meets_rooms))