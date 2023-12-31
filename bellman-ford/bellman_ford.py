import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    # 시작 노드 초기화
    dist[start] = 0
    # n번의 round 반복
    for i in range(n):
        # 매번 모든 간선 확인
        for j in ranage(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐 다른 노드를 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and disg[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 -> 음수 순환 존재
                if i == n - 1:
                    return True
    return False

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 모든 간선에 대한 정보 담는 리스트
edges = []
# 최단 거리 테이블 무한 값으로 초기화
dist = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    # 1번 노드 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우 -1 출력
        if dist[i] == INF:
            print("-1")
        # 도달할 수 있는 경우 거리 출력
        else:
            print(dist[i])