#Brute Force Approach
#Time complexity: O(n^2)
def checkInclusion(s1, s2):
    from collections import Counter
    s1_count = Counter(s1)
    n = len(s2)
    k = len(s1)

    for i in range(n - k + 1):
        window_count = Counter(s2[i:i+k])
        if window_count == s1_count:
            return True

    return False


#567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        k=len(s1)
        l=0
        dici={}
        di={}
        for i in s1:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        for r in range(n):
            if s2[r] not in dici:
                dici[s2[r]]=1
            else:
                dici[s2[r]]+=1
            if (r-l==k):
                if dici[s2[l]]==1:
                    del dici[s2[l]]
                else:
                    dici[s2[l]]-=1
                l+=1
            if di == dici:
                return True
        return False           
        
# Example usage:
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"

print(solution.checkInclusion(s1, s2))  # Output: True

