class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            //cout << "false" << endl;
            return false;
        }
        int op = x;
        int rx = 0;
        while(true){
            rx = rx + op%10 ;
            op /= 10;
            if(op == 0)
                break;
            if(rx > INT_MAX/10 || (rx == INT_MAX/10 && op%10>7)){
                return false;
            }
            rx = rx * 10;
        }
        if(rx == x){
            //cout << "true" << endl;
            return true;
        }
        else{
            //cout << "false" << endl;
            return false;
        }
    }
};
