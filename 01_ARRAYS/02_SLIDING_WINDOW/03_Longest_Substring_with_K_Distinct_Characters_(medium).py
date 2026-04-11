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
5             
# Example usage:
s = "eceba" 
k = 2
print(BruteLongestSubstringKDistinct(s, k))  # Output: 3 (substring "ece" has 2 distinct characters)




#300. Longest Substring with At Most K Distinct Characters 

# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters. 

#optimal Approach (Sliding Window)
# Time Complexity: O(n)

def LongestSubstringKDistinct(s, k):
    left = 0
    max_length = 0
    char_count = {}.

    for right in range(len(s)):
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        if len(char_count) == k:
          max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "eceba"
k = 2
print(LongestSubstringKDistinct(s, k))  # Output: 3 (substring "ece" has 2 distinct characters)