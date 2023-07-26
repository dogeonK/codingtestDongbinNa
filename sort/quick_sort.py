array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 한 개인 경우
        return
    
    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        while(left <= end and array[left] <= array[pivot]): # 피벗보다 큰 값 찾기
            left += 1
        while(right > start and array[right] >= array[pivot]): # 피벗보다 작은 값 찾기
            right -= 1
        
        if left > right:    # 위치 엇갈린 경우 -> 피벗과 피벗보다 작은 값의 위치 변경
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 위치 안엇갈린 경우 -> 피벗보다 작은 값, 피벗보다 큰 값 위치 변경
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 묶음과 오른쪽 묶음 각각 정렬
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)