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



# prefix and suffix code snippets are provided for context, but they are not directly related to the Maximum Product Subarray problem.



# 👉 You’re thinking:
# “If we multiply all elements, prefix and suffix will give same values… so why answer changes?”

# Let’s fix that clearly 👇

# ❗ Key Point

# 👉 Prefix and suffix are NOT always giving same intermediate values

# They only become same if:

# No zeros
# Even number of negatives
# Whole array is optimal

# Otherwise → they behave differently

# 🔥 Why answer can change

# Because:

# 👉 Maximum product subarray is NOT always the whole array

# So:

# Prefix may include a bad part at start
# Suffix may skip that and give better result
# ⚡ Example where they DIFFER
# nums = [2, -5, -2, -4, 3]
# 🔹 Prefix (Left → Right)
# 2
# 2 * -5 = -10
# -10 * -2 = 20 ✅
# 20 * -4 = -80
# -80 * 3 = -240

# 👉 Max from prefix = 20

# 🔹 Suffix (Right → Left)
# 3
# 3 * -4 = -12
# -12 * -2 = 24 ✅🔥
# 24 * -5 = -120
# -120 * 2 = -240

# 👉 Max from suffix = 24

# 🎯 Final Answer = 24

# 👉 So both directions are NOT same
# 👉 They produce different peaks

# 💡 Why this happens

# 👉 There are odd number of negative elements

# If you include all → result becomes negative
# So best subarray =
# drop either prefix part OR suffix part
# 🧠 Thinking Visualization

# Array:

# [2, -5, -2, -4, 3]

# Negatives = 3 (odd)

# 👉 To get max:

# Remove leftmost negative → suffix helps
# OR
# Remove rightmost negative → prefix helps
# ⚡ When both are SAME

# Example:

# nums = [2, 3, 4]

# Prefix:

# 2 → 6 → 24

# Suffix:

# 4 → 12 → 24

# 👉 Same answer (whole array is best)

# 🧠 Core Insight

# Max Product=max(product after removing prefix, product after removing suffix)

# 🔥 Final Intuition

# 👉 Prefix = “remove bad suffix”
# 👉 Suffix = “remove bad prefix”

# One of them will give correct answer

# 🎯 One-line Answer (Exam Ready)

# 👉 “Prefix and suffix give different results when negative numbers or zeros exist, because optimal subarray may exclude either prefix or suffix part.”

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        prefix = 1
        suffix = 1
        ans = float('-inf')
        
        for i in range(n):
            # if zero comes, reset
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            
            ans = max(ans, prefix, suffix)
        
        return ans
    
# Example usage:
solution = Solution()
nums = [2,3,-2,4]
print(solution.maxProduct(nums))  # Output: 6 (subarray [2,3])