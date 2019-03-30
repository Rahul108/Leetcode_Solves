class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s == ""){
            return 0;
        }
        int n=s.length();
        int cur_length = 1;
        int max_length = 1;
        int prev_index;
        int i;
        int visited[256];
        bool flag = false;

        for(i=0;i<256;i++){
            visited[i]=-1;
        }

        visited[s[0]] = 0;

        for(i=1;i<n;i++){
            prev_index = visited[s[i]];
            if(prev_index == -1 || i-cur_length > prev_index){
                cur_length++;
            }
            else{
                if(flag==false)
                    flag = true;
                if(cur_length > max_length){
                    max_length = cur_length;
                }
                cur_length =  i - prev_index;
            }
            visited[s[i]] = i;
        }
        if(cur_length > max_length){
                    max_length = cur_length;
        }
        return max_length;
        //if(flag)
            //return cur_length;
        //else
            //return max_length;
    }
};
