#Brute Force Approach
#Time complexity: O(n^2)
def findAnagrams(s, p):
    from collections import Counter
    p_count = Counter(p)
    n = len(s)
    k = len(p)
    result = []

    for i in range(n - k + 1):
        window_count = Counter(s[i:i+k])
        if window_count == p_count:
            result.append(i)

    return result


# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str):
        n=len(s)
        l=0
        k=len(p)
        dici={}
        di={}
        for i in p:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        result=[]
        for r in range(n):
            if s[r] not in dici:
                dici[s[r]]=1
            else:
                dici[s[r]]+=1
            if (r-l==k):
                if dici[s[l]]==1:
                    del dici[s[l]]
                else:
                    dici[s[l]]-=1
                l+=1
            if di== dici:
                result.append(l)
        return result



# Example usage:
solution = Solution()
s = "cbaebabacd"
p = "abc"

print(solution.findAnagrams(s, p))  # Output: [0, 6]