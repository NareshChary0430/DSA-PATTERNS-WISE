# Minimum Subarray Problem Brute Force Approach:
# Time complexity: O(n^2)

def minSubArray(nums):
    n = len(nums)
    min_sum = float('inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            min_sum = min(min_sum, current_sum)

    return min_sum



# optimal appraoch for Minimum Subarray problem is Kadane's Algorithm

from typing import List

#User function Template for python3


class Solution:
    def smallestSumSubarray(self, nums, N):
        #Your code here
        bestEnding = nums[0]
        ans = nums [0]

        for i in range(1,len(nums)):
            v1 = bestEnding + nums[i]
            v2 = nums[i]

            bestEnding = min(v1,v2)
            ans = min(ans,bestEnding)
        return ans
        
# Example usage:
solution = Solution()
nums = [1, -2, 3, -4, 5]
print(solution.smallestSumSubarray(nums, len(nums)))  # Output: -4 (subarray [-4])
