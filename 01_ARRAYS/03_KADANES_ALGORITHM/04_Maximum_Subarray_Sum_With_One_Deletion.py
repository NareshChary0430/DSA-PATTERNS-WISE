#Brute Force Approach
#Time complexity: O(n^2)



class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        res = float('-inf')

        for i in range(n):
            for j in range(i, n):
                
                # Case 1: no deletion
                subarray_sum = sum(arr[i:j+1])
                res = max(res, subarray_sum)

                # Case 2: delete one element
                for k in range(i, j+1):
                    temp = subarray_sum - arr[k]
                    res = max(res, temp)

        return res
    






# 1186. Maximum Subarray Sum with One Deletion
# Given an array of integers, return the maximum sum for a non-empty subarray (containing at most one deletion of an element).  

#optimal approach for Maximum Subarray Sum with One Deletion problem is Kadane's Algorithm




from typing import List


class Solution:
    def maximumSum(self, arr:   List[int]) -> int:
        noDel = arr[0] 
        oneDel = float('-inf') 
        res = arr[0]


        for i in range(1,len(arr)):

            prevNodelete = noDel
            prevOnedelete = oneDel

            noDel = max(noDel+arr[i],arr[i])

            oneDel = max(prevOnedelete + arr[i],prevNodelete)

            res = max(res,noDel,oneDel)
        
        return res
    
# Example usage:
solution = Solution()
arr = [1,-2,0,3]
print(solution.maximumSum(arr))  # Output: 4 (subarray [1,0,3] with deletion of -2)

