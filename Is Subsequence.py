class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS = 0
        pointerT = 0
        
        while pointerS<len(s) and pointerT<len(t):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
            pointerT += 1
        
        return pointerS == len(s)