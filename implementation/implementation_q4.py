"""
# [문제] 문자열 재정렬

- 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
- 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
"""

n = input()

n_list = []

sum_result = 0

for i in range(len(n)):
    if n[i].isalpha():
        n_list.append(ord(n[i]))
    elif n[i].isdigit():
        sum_result += int(n[i])

n_list.sort()

for ascii in n_list:
    print(chr(ascii), end="")

if sum_result != 0:
    print(sum_result)
else:
    print()