class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1){
            return s;
        }
        string ms;
        int lng = s.size();
        int cln = 2 * numRows - 2 ;
        for(int i=0; i<numRows; i++){
            for(int j=0; j+i< lng; j+=cln){
                ms += s[j+i];
                if(i!=0 && i!= numRows-1 && (j+cln-i)<lng){
                    ms += s[j+cln-i];
                }
            }
        }
        return ms;
    }
};
