class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       if(strs.empty()){
           return "";
       } 
       if(strs.size()==1){
           return strs[0];
       }
        
        int tot_len = strs.size();
        int min_len = strs[0].size();
        
        
        for(int i=0;i<tot_len-1;i++){
            if(strs[i].empty()){
                return "";
            }
            
            if(strs[i][0] != strs[i+1][0])
                return "";
            int chk(0);
            while(true){
                if(strs[i][chk] == strs[i+1][chk]){
                    if(min_len >= chk+1 )
                        chk++;
                    else
                        break;
                    
                }
                else
                    break;
            }
            min_len = (chk < min_len) ? chk : min_len;
        }
        
        return strs[0].substr(0,min_len);
        
        
    }
};
