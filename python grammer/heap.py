import heapq
import time

#측정 시작
start_time = time.time()

# 최소 힙
def heapsort(iterable):
    h = []
    result = []

    # 모든 원소 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 워소 차례대로 꺼내서 result에 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

print(result)

#측정 종료
end_time = time.time()

#수행 시간 출력
print(f"time : {end_time - start_time}")

# 최대 힙
def heapsort2(iterable):
    h = []
    result = []

    # 모든 원소 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 워소 차례대로 꺼내서 result에 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
