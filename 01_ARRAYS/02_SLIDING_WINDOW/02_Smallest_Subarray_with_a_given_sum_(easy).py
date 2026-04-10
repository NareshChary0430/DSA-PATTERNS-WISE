#209. Minimum Size Subarray Sum Brute Force Approach 
# Time Complexity: O(n^2)


def BruteminSubArrayLen(target, nums):
    n = len(nums)
    min_len = float('inf')

    for i in range(n):
        current_sum = 0

        for j in range(i, n):
            current_sum += nums[j]

            if current_sum >= target:
                min_len = min(min_len, j - i + 1)
                break

    return 0 if min_len == float('inf') else min_len




# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead. 


#optimized Approach (Sliding Window)
# Time Complexity: O(n)
def minSubArrayLen( target , nums ):
        n = len(nums)
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(n):
            window_sum += nums[right]

            # shrink window from left while sum >= target
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


# Example usage:
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))  # Output: 2 (subarray [4,3] has sum >= 7)