class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n))
        ones=0
        for i in n:
            if i=="1":
                ones+=1
        return ones
