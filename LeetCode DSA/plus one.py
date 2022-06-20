class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=""
        s=list(map(str,digits))
        for i in s:
            ans+=i
        res=list(str(int(ans)+1))
        return res
