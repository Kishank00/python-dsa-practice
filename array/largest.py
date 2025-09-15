nums = [22, 44, 12, 10, 56, 84, 99, 66, 30, 102]

class Solution:

    def largest_element(self, nums):
        n = len(nums)
        largest = float("-inf")

        for i in range(0, n):
            largest = max(largest, nums[i])

        return largest

s = Solution()
print(s.largest_element(nums))