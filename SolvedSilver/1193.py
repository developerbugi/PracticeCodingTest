"""
짝수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소하며

홀수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 늘어난다.

대각선에서 홀수 번째의 위치에 존재하면 오름차순, 짝수번째는 내림차순으로 되어 있음
"""

n = int(input())

line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    a = n
    b = line - n + 1
else:
    a = line - n + 1
    b = n

print(a, '/', b, sep='')