nums = [4, 8, 1, 3, 9, 2, 6]

# ascending order
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

bubble_sort(nums)
print(nums)

# descending order
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


bubble_sort(nums)
print(nums)