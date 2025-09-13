nums = [4, 8, 1, 3, 9, 2, 6]


# ascending order
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

insertion_sort(nums)
print(nums)

# descending order
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] < key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

insertion_sort(nums)
print(nums)