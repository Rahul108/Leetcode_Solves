class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        long long int n = nums1.size();
        long long int m = nums2.size();
        
        vector<int> temp1;
        
        if(n>m){
            for(int i=0;i<nums1.size();i++)
                temp1.push_back(nums1[i]);
            nums1.clear();
            for(int i=0;i<nums2.size();i++){
                nums1.push_back(nums2[i]);
            }
            nums2.clear();
            for(int i=0;i<temp1.size();i++)
                nums2.push_back(temp1[i]);
            temp1.clear();
            int tt;
            tt = n;
            n = m;
            m = tt;
        }
        
        if(n==0){
            if(m%2!=0)
                return nums2[m/2];
            else
                return double(nums2[m/2]+nums2[m/2 - 1])/2;
        }
        
        if(m==0){
            if(n%2!=0)
                return nums1[n/2];
            else
                return double(nums1[n/2]+nums1[n/2 - 1])/2;
        }
        
        long long int start_ind = 0;
        long long int end_ind = n;
        long long int i,j,md;
        
        while(start_ind <= end_ind){
            i = (start_ind + end_ind) / 2;
            j = ((n + m + 1) / 2) - i;
            
            if(j<0){
                end_ind = i - 1;
                continue;
            }

            if (i < n && j > 0 && nums2[j - 1] > nums1[i])
                start_ind = i + 1;

            else if (i > 0 && j < m && nums2[j] < nums1[i - 1] && j>=0)
                end_ind = i - 1;
            
            else if(i>0 && j<0)
                end_ind = i - 1;

            else
            {
                if (i == 0)
                    md = nums2[j - 1];
                else if (j == 0)
                    md = nums1[i - 1];
                else
                    md = max(nums1[i - 1], nums2[j - 1]);
                break;
            }
        }
        if ((n + m) % 2 == 1)
        return (double)md;

        if (i == n)
            return (md+nums2[j]) / 2.0;

        if (j == m)
            return (md + nums1[i]) / 2.0;

        return (md + min(nums1[i], nums2[j])) / 2.0;
    }
};
