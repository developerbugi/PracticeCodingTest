def findLargestSquareSize(samples):
    # 제품 샘플이 비어있는 경우 0 반환
    if not samples:
        return 0

    n = len(samples)  # 샘플의 크기 파악

    DP = [[0]*n for _ in range(n)]  # DP를 위한 n x n 매트릭스 생성, 초기값은 모두 0

    max_size = 0  # 최대 정사각형의 크기를 저장할 변수 초기화

    # 샘플의 모든 요소를 순회
    for i in range(n):
        for j in range(n):
            if samples[i][j] == 1:  # 현재 요소가 불량 제품(1)인 경우
                if i == 0 or j == 0:  # 첫 번째 행이나 첫 번째 열인 경우, 불량 제품의 크기는 자기 자신
                    DP[i][j] = samples[i][j]
                else:
                    # 왼쪽 위 대각선, 바로 위, 바로 왼쪽 요소 중 최소값에 1을 더한 값을 현재 위치에 저장
                    DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1

                # 최대 정사각형의 크기 업데이트
                max_size = max(max_size, DP[i][j])

    return max_size  # 최대 정사각형의 크기 반환