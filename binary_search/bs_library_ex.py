from bisect import bisect_right, bisect_left

# 값이 [left_value, right_value]인 데이터의 개수 반환 함수
def range_count(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(range_count(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(range_count(a, -1, 3))