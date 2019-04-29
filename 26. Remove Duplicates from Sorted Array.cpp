class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        int p1=0,p2=1;
        for(;p2<nums.size();p2++){
            if(nums[p2]!=nums[p1]){
                p1++;
                nums[p1]=nums[p2];
            }
        }
        return p1+1;
    }
};
