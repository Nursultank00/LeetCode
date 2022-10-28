class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        
        longest = 0
        left = 0
        chars = {}
        for ind, char in enumerate(s):
            if char in chars:
                left = max(left, chars[char] + 1)
            chars[char] = ind
            cur = ind + 1 - left
            longest = max(cur, longest)
        return longest