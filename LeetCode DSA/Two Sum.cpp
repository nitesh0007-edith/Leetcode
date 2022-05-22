class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> results;
        int l=size(nums);
        for(int i=0;i<l-1;i++)
        {
            for(int j=l-1;j>i;j--)
            {
                if(nums[i]+nums[j]==target){
                    results.push_back(i);
                    results.push_back(j);
                }
            }
}
        return results;
        
    }
};
