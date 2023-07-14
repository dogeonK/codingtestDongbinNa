"""
# [문제] 왕실의 나이트

- 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면입니다. 왕실 정원의 특정한 한 칸에 나이트가 서있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
- 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
- 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
- 이처럼 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요. 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현합니다.
"""

n = input()
col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

n_column, n_row = int(col_list.index(n[0])) + 1, int(n[1])

count = 0

night_move_dx = [1 , 2, -1, -2, 1, 2, -1, -2]
night_move_dy = [2 , 1, 2, 1, -2, -1, -2, -1]

for i in range(8):
    col_point = n_column + night_move_dx[i]
    row_point = n_row + night_move_dy[i]
    if col_point < 1 or col_point > 8 or row_point < 1 or row_point > 8:
        continue
    count += 1

print(count)