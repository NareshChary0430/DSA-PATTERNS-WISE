class Solution:
    def longestOnes(self, nums, k):
        n=len(nums)
        l=0
        temp=0
        ans=0
        # nums.sort()
        for r in range(n):
            if nums[r] == 0:
                temp+=1
            while (temp>k):
                if nums[l]==0:
                    temp-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans          


# Example usage:
solution = Solution()
nums = [1, 1, 0, 0, 0, 1, 1]
k = 2
print(solution.longestOnes(nums, k))  # Output: 4