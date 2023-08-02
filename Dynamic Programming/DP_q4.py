"""
# [문제] 금광

- n x m 크기의 금광이 있습니다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
- 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
- 이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다. 결과적으로 **채굴자가 얻을 수 있는 금의 최대 크기**를 출력하는 프로그램을 작성하세요.
"""

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    gold_list = list(map(int, input().split()))

    d = []
    index = 0

    for i in range(n):
        d.append(gold_list[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = d[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = d[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = d[i][j - 1]

            d[i][j] = d[i][j] + max(left_up, left, left_down)
    
    result = 0
    for i in range(n):
        result = max(result, d[i][m - 1])
    
    print(result)