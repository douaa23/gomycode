1//
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(binary_search([1, 2, 3, 5, 8], 6)) 
print(binary_search([1, 2, 3, 5, 8], 5))  
2//
def power(a, b):
    return a ** b
print(power(3, 4))  ''' 81'''
3//
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
bubble_sort(sample_data)
print(sample_data)  
4//
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
merge_sort(sample_data)
print(sample_data) 
5//
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
sorted_data = quick_sort(sample_data)
print(sorted_data)
