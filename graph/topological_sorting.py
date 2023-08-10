from collections import deque

# 노드의 개수, 간선의 개수 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 간선 정보 입력받기
for _ in range(e):
    # 정점 A에서 B로 이동 가능
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입 차수 1 증가
    indegree[b] += 1

#위상 정렬
def topological_sort():
    result = [] # 알고리즘 수행 결과 담을 리스트
    q = deque() # 큐 기능 위한 deque 라이브러리 사용
    
    # 진입차수 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        
        # 해당 원소에 연결된 노드들 진입차수 1 감소
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수 0이되면 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topological_sort()