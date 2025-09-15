# Check whether the array is sorted or not

arr = [1, 2, 3, 4, 5, 6]

class Solution:

    def sorted_arr(self, arr):
        n = len(arr)

        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                return False

        return True

s = Solution()
print(s.sorted_arr(arr))