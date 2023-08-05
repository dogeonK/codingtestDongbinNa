import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한 값 의미로 10억 설정

# 노드와 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용은 c이다.
    graph[a].append((b, c))

"""
이 부분까지는 앞에서 한 다익스트라 알고리즘 구현 방식과 똑같음
방문 처리 목적인 visited,
최단 거리 구하는 get_smallest_node() 사용하지 않음
"""

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 -> 0으로 설정, 우선수위 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # 우선순위 큐 빌 때까지 반복
    while q:
        # 최단 거리 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있다면 무시한다.
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 최단 거리 갱신되는 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])