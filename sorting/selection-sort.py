nums = [4, 8, 1, 3, 9, 2, 6]

# ascending order
def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i],nums[min_index] = nums[min_index], nums[i]

selection_sort(nums)
print(nums)

# descending order
def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] > nums[min_index]:
                min_index = j

        nums[i],nums[min_index] = nums[min_index], nums[i]

selection_sort(nums)
print(nums)