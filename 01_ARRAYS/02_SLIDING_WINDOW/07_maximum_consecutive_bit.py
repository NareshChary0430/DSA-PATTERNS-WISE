class Solution:
    def maxConsecBits(self, nums):
        count0 = 0
        count1 = 0
        maxi = 0

        for num in nums:
            if num == 1:
                count1 += 1
                count0 = 0
            else:
                count0 += 1
                count1 = 0

            maxi = max(maxi, count0, count1)

        return maxi
    
# Example usage:
solution = Solution()
nums = [1, 1, 0, 0, 0, 1, 1]
print(solution.maxConsecBits(nums))  # Output: 3




