
# Given a string s, find the length of the longest substring without repeating characters.

#Brute Force Approach
# Time Complexity: O(n^3)
def BruteLongestSubstring(s):
    n = len(s)
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            distinct_chars = set(substring)

            if len(distinct_chars) == len(substring):
                max_length = max(max_length, j - i + 1)

    return max_length

# Example usage:
s = "abcabcbb"
print(BruteLongestSubstring(s))  # Output: 3 (substring "abc" has no repeating characters)





#optimal Approach (Sliding Window)
# Time Complexity: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)
        return max_length
    
# Example usage:
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))  # Output: 3 (substring "abc" has no repeating characters)