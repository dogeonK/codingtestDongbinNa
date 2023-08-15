# 데이터의 개수 N과 데이터 입력받기
n = 5
data = [10, 20, 30, 40, 50]

# Prefix Sum 구하기
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left, right = map(int, input().split())
print(prefix_sum[right] - prefix_sum[left - 1])