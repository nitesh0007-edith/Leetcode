class Solution:
    def lengthOfLastWord(self, s: str) -> int:       
        l1=s.split()
        if len(s)==0:
            return 0
        return len(l1[-1])
