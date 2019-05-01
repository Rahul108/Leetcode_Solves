class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()) return 0;
        return (int)haystack.find(needle);
    }
};
