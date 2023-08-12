import math

n = int(input())
# 모든 수가  소수(True)인 것으로 초기화
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i 제외한 i의 배수 제거
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i] == True:
        print(i, end=" ")