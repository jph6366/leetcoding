
#include "../include/is_subsequence.hpp"

namespace cppbase
{

 //! Compute if s is a subsequence of t
//  1. We treat subsequence string as stack and traverse from end of base string
//  2. When the top of stack matches current element in base string we pop()
//  3. We continue till we reach end of base string or till stack becomes empty

 bool isSubsequence(std::string s,  std::string t)
{
    // if (s.length() == 0) return true;

    // int ptr = 0;
    // for(int i = 0; i < t.length(); i++)
    // {
    //     if (t[i] == s[ptr])
    //     {
    //         ptr++;
    //         if (ptr == s.length()) return true;
    //     } 
    // }

    // return false;

    for(int x=t.size()-1; x>=0 && !s.empty(); x--) {
        if ( t[x] == s[s.size()-1]) {
            s.pop_back();
        }
    }

    return s.empty();

}

} // namespace cppbase
