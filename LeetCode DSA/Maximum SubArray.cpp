/* Naive Solution having N^2 complexity */

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res=nums[0];
        for(int i=0;i<nums.size();i++)
        {
            int curr=0;
            for(int j=i;j<nums.size();j++)
            {
                curr=curr+nums[j];
                res=max(res,curr);
            }
        }
        return res;
        
    }
};

/* Efficient Solution O(n) using kadan's Algorithms */

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res=nums[0];
        int maxEnd=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            maxEnd=max(maxEnd+nums[i],nums[i]);
            res=max(res,maxEnd);
        }
        return res;
        
    }
};
