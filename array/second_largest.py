nums = [22, 44, 12, 10, 56, 84, 99, 66, 30, 102, 101]

class Solution:

    def second_largest(self, nums):
        n = len(nums)
        largest = float("-inf")
        sec_largest = float("-inf")

        for i in range(0, n):
            if nums[i] > largest:
                sec_largest = largest
                largest = nums[i]

            elif nums[i] > sec_largest and nums[i] != largest:
                sec_largest = nums[i]

        return sec_largest

s = Solution()
print(s.second_largest(nums))
                