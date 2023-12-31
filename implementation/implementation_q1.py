"""
# [문제] 상하좌우

- 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다.
- 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.
- 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있습니다.
    - L : 왼쪽으로 한 칸 이동
    - R : 오른쪽으로 한 칸 이동
    - U : 위로 한 칸 이동
    - D : 아래로 한 칸 이동
- 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 예를 들어 (1, 1)의 위치 에서 L 혹은 U를 만나면 무시됩니다.
"""

n = int(input())
move = list(map(str, input().split()))

x, y = 1, 1

for i in move:
    if i == 'L' and y > 1:
        y -= 1
    elif i == 'R' and y < 5:
        y += 1
    elif i == 'U' and x > 1:
        x -= 1
    elif i == 'D' and x < 5:
        x += 1
    else:
        continue

print(x, y)