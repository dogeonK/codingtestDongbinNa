"""
# [문제] 정렬된 배열에서 특정 수의 개수 구하기

- N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
- 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
- 단, 이 문제는 시간 복잡도 $O(log{N})$으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.
"""
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def range_count(array, x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)

    return right_index - left_index

print(range_count(array, x))