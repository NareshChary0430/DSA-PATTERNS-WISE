# Maximum Subarray Problem Brute Force Approach:
# Time complexity: O(n^2)

def maxSubArray(nums):
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum



  
# optimal appraoch for Maximum Subarray problem is Kadane's Algorithm
# The idea is to keep track of the maximum sum of a subarray that ends at the current index.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        bestEnding = nums[0]
        ans = nums [0]

        for i in range(1,len(nums)):
            v1 = bestEnding + nums[i]
            v2 = nums[i]

            bestEnding = max(v1,v2)
            ans = max(ans,bestEnding)
        return ans
        
# Example usage:
solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))  # Output: 6 (subarray [4,-1,2,1])
