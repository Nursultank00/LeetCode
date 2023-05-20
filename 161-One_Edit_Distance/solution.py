class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False
        i = j = edits = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i, j = i + 1, j + 1
                continue
            edits += 1
            if edits > 1:
                return False
            if len(s) == len(t):
                i, j = i + 1, j + 1
            else:
                if len(s) > len(t):
                    i += 1
                else:
                    j += 1
        if i < len(s) or j < len(t):
            edits += 1
        return edits == 1