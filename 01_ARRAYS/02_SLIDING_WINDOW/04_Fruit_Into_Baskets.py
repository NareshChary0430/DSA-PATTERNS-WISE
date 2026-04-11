#Brute Force Approach
# Time Complexity: O(n^3)

def BruteLongestSubstringKDistinct(s, k):
    n = len(s)
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            distinct_chars = set(substring)

            if len(distinct_chars) <= k:
                max_length = max(max_length, j - i + 1)

    return max_length

# Example usage:
s = "eceba"
k = 2
print(BruteLongestSubstringKDistinct(s, k))  # Output: 3 (substring "ece" has 2 distinct characters)


# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit. 

# You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

#optimal Approach (Sliding Window)
# Time Complexity: O(n)

class Solution:
    def totalElements(self, arr):
        # Code here
        
        left = 0
        n = len(arr)
        dici = {}
        
        max_len = 0 
        
        for high in range(n):
            if arr[high] in dici:
                dici[arr[high]]+=1
            else:
                dici[arr[high]]=1
            
            while len(dici) > 2:
                dici[arr[left]] -= 1
                
                if dici[arr[left]] == 0:
                    del dici[arr[left]]
                left+=1
            
            max_len = max(max_len,high-left+1)
        
        return max_len
    
# Example usage:
arr = [1, 2, 1, 3, 4]
solution = Solution()
print(solution.totalElements(arr))  # Output: 3 (subarray [1, 2, 1] has at most 2 distinct elements)