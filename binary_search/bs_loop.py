def binary_search(arrary, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arrary[mid] == target:
            return mid
        elif arrary[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None

# 원소의 개수 n, 찾고자 하는 값 target
n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않음")
else:
    print("해당 원소 {}은 {}번째에 있으며, 인덱스 값은 {}입니다.".format(target, result + 1, result))