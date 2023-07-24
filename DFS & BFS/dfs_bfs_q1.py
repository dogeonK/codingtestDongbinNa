"""
# [문제] 음료수 얼려 먹기

- N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
- 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
- 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
"""

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: return False

    if ice_array[x][y] == 0:
        ice_array[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

count = 0

n, m = map(int, input().split())

ice_array = []

for i in range(n):
    ice_array.append(list(map(int, input())))

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)