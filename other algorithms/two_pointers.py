# 데이터 개수
n = 5
# 찾고자 하는 부분합
m = 5

data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start 증가시키면서 반복
for start in range(n):
    # end 최대한 이동
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)