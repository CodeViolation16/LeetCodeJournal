# the clever trick here is that they move the cursor along the 2 array, very clever.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0, 0 
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+= 1
            j+= 1
        return True if i == len(s) else False
