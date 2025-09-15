arr = [4, 8, 1, 3, 9, 2, 6]

# Dividing the array
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_half = merge_sort(left_arr)
    right_half = merge_sort(right_arr)

    return merge_array(left_half, right_half)

# Merge Sort code

def merge_array(left, right):
    result = []
    i = j = 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result

print(merge_sort(arr))