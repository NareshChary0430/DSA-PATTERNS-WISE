#Bruet force solution
# Time Complexity: O(n^2)

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            pro = 1
            for j in range(i, n):
                pro = pro * nums[j]

                if pro < k:
                    count += 1
                else:
                    break
        return count

# Example usage:
nums = [10, 5, 2, 6]
k = 100
solution = Solution()
print(solution.numSubarrayProductLessThanK(nums, k))  # Output: 8

# optimal solution
# Time Complexity: O(n)

# Given an array of positive integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        n = len(nums)
        low = 0
        pro = 1
        count = 0 

        for high in range(n):
            
            pro  = pro * nums[high]

            while pro >= k:
                pro = pro / nums[low]
                low += 1
            
            count = count + (high - low + 1)
        return count

# Example usage:
nums = [10, 5, 2, 6]
k = 100
solution = Solution()
print(solution.numSubarrayProductLessThanK(nums, k))  # Output: 8     