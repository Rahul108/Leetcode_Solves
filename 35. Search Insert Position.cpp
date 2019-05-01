class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int ln=nums.size();
        int lw=0,hw=ln-1;
        while(lw<=hw){
            int ps=(lw+hw)/2;
            if(nums[ps]<target)
                lw=ps+1;
            else
                hw=ps-1;
        }
        return hw+1;
    }
};
