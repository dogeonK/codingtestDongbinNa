INF = int(1e9) # 무한 의미로 10억 사용

# 노드의 개수 및 간선의 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현) 만들기, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 0으로 설정
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보 입력 받기, 해당 값으로 설정
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과값 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 도달할 수 없는 경우 INF
        if graph[i][j] == INF:
            print("INF")
        else:
            print(graph[i][j], end=" ")
    print()