import math

# 소수 판별 함수 (2이상의 자연수)
def is_prime(x):
    # 2부터 x 제곱근까지 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어지면 소수 아님
        if x % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(1000))