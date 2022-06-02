class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=nums[0]
        n1=[]
        n1.append(nums[0])
        for i in range(1,len(nums)):
            sum+=nums[i]
            n1.append(sum)
        return n1
