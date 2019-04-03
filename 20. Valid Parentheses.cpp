class Solution {
public:
    bool isValid(string s) {
        stack<char> br;
        for(int i=0;i<s.length();i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                br.push(s[i]);
            }
            else{
                if(br.empty())
                    return false;
                if( (s[i]==')' && br.top()=='(') || (s[i]=='}' && br.top()=='{') || (s[i]==']' && br.top()=='[') ){
                    //cout <<"Before pop:" << br.top()<<endl;
                    br.pop();
                }
                else{
                    //cout << "false" << endl;
                    return false;
                }
            }
        }
        if(br.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};
