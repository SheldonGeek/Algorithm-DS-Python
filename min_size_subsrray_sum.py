'''
find min size of sub array which has total sum s >= k
[1,2,3,2,3,4] k =7, n = 2
'''

class Solution:
    def find_min_size_subarray(self, nums, k):
        if nums is None or len(nums) == 0:
            return -1
        n = len(nums)
        j = 0
        s = 0
        min_len = n + 1
        for i in range(n):
            while j < n-1 and s < k:
                s += nums[i]
                j += 1
            if s >= k:
                min_len = min(min_len, j - i)

        if min_len == n+1:
            return -1
        return min_len

