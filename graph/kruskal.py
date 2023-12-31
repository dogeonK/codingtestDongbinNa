# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드 찾을 때까지 재귀 호출
    if parent[x]!= x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)
# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선을 담을 리스트, 최종 비용 담을 변수
edges = []
result = 0

# 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선 비용순으로 정렬
edges.sort()

# 간선의 개수만큼 반복
for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않을 시 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)