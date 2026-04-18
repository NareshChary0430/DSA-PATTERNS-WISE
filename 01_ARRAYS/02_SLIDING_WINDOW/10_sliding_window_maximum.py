#brute force approach

def maxSlidingWindow(nums, k):
    n = len(nums)
    max_window = []
    
    for i in range(n - k + 1):
        window_max = max(nums[i:i+k])
        max_window.append(window_max)
    
    return max_window

# Example usage:
nums = [1, 3, -1, -3, 5, 3
, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]




#optimal solution using deque 

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):

        n=len(nums)
        res=[0]*(n-k+1)
        deq=deque()
        for r in range(n):
            while deq and deq[0]<=r-k:
                deq.popleft()
            while deq and nums[deq[-1]]<nums[r]:
                deq.pop()
            deq.append(r)
            if r>=k-1:
                res[r-k+1]=nums[deq[0]]
        return res
        
# Example usage:
solution = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(solution.maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]