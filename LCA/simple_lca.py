import sys
sys.setrecursionlimit(int(1e9)) # 런타임 오류 피하기
n = int(input())

parent = [0] * (n + 1)  # 부모 노드 정보
d = [0] * (n + 1)   # 각 노드까지의 깊이
c = [0] * (n + 1)   # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구한 경우
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상 찾는 함수
def lca(a, b):
    # 깊이 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent(a)
        else:
            b = parent(b)
    # 노드 같아지도록
    while a != b:
        a = parent(a)
        b = parent(b)
    return a

dfs(1, 0)   # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))