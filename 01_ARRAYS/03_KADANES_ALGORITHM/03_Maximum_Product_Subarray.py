#Brute Force Approach
#Time complexity: O(n^2)
def maxProduct(nums):
    n = len(nums)
    max_product = float('-inf')

    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= nums[j]
            max_product = max(max_product, current_product)

    return max_product



# Maximum Product Subarray
# The idea is to keep track of both the maximum and minimum product of a subarray that ends at the current index, because a negative number can turn a minimum product into a maximum product and vice versa.

# Time complexity: O(n)
#optimal approach for Maximum Product Subarray problem is Kadane's Algorithm

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        maxEnding = nums[0]
        minEnding = nums[0]

        ans = nums[0]

        for i in range(1,len(nums)):

            v1 = nums[i]
            v2 = nums[i] * maxEnding
            v3 = nums[i] * minEnding 

            maxEnding = max(v1,v2,v3)
            minEnding = min(v1,v2,v3)

            ans = max(ans,maxEnding)
        
        return ans
    
# Example usage:
solution = Solution()
nums = [2,3,-2,4]
print(solution.maxProduct(nums))  # Output: 6 (subarray [2,3])


