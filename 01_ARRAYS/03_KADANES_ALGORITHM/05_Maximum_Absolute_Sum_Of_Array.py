#Brute Force Approach for Maximum Absolute Sum of Any Subarray problem is to calculate the sum of all possible subarrays and keep track of the maximum absolute sum encountered. This approach has a time complexity of O(n^2) due to the nested loops required to generate all subarrays and calculate their sums.


def maxAbsoluteSum(nums):
    n = len(nums)
    max_abs_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_abs_sum = max(max_abs_sum, abs(current_sum))

    return max_abs_sum








# 1749. Maximum Absolute Sum of Any Subarray
# Given an integer array nums, return the maximum absolute sum of any subarray of nums. 

#optimal approach for Maximum Absolute Sum of Any Subarray problem is Kadane's Algorithm

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        

        maxSum = float("-inf")
        minSum = float("inf")

        curr_Maxsum = 0
        curr_Minsum = 0 
        res = 0

        for i in range(len(nums)):

            curr_Maxsum = max(nums[i] , curr_Maxsum + nums[i] )

            maxSum = max(maxSum,curr_Maxsum)

            curr_Minsum = min(nums[i], curr_Minsum+nums[i])

            minSum = min(minSum,curr_Minsum)

            res = max(abs(maxSum) , abs(minSum))

        return res      
    

# Example usage:
solution = Solution()
nums = [1,-3,2,3,-4]
print(solution.maxAbsoluteSum(nums))  # Output: 5 (subarray [2,3] has sum 5, and subarray [-3,-4] has sum -7, so the maximum absolute sum is 7)
