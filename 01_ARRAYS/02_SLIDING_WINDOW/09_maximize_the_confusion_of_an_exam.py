#Brute force approach
#Time complexity: O(n^2)
def maxConsecutiveAnswers(nums, k):
    n = len(nums)
    max_length = 0

    for i in range(n):
        countT = 0
        countF = 0

        for j in range(i, n):
            if nums[j] == 'T':
                countT += 1
            else:
                countF += 1

            if min(countT, countF) <= k:
                max_length = max(max_length, j - i + 1)
            else:
                break

    return max_length




#optimal approach
class Solution:
    def maxConsecutiveAnswers(self, nums, k):
        n=len(nums)
        l=0
        cnt1=0
        cnt0=0
        ans=0
        # nums.sort()
        for r in range(n):
            if nums[r] == 'F':
                cnt0+=1
            else:
                cnt1+=1
            while (min(cnt1,cnt0)>k):
                if nums[l]== 'F':
                    cnt0-=1
                else:
                    cnt1-=1
                l+=1
            ans =max(ans,r-l+1)
        return ans          

# Example usage:
solution = Solution()
nums = ['T', 'T', 'F', 'F', 'F', 'T', 'T']
k = 2

print(solution.maxConsecutiveAnswers(nums, k))  # Output: 5