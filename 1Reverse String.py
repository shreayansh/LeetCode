class Solution:
    def reverseString(self, s: List[str]):
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]