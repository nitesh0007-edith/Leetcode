class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=len(strs)
        pre=""
        if l==0:
            return ""
        if l==1:
            return strs[0]
        strs.sort()
        end=min(len(strs[0]),len(strs[l-1]))
        i=0
        while(i<end and strs[0][i]==strs[l-1][i] ):
            i=i+1
        pre=strs[0][0:i]
        return pre
