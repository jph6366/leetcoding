
#include "../include/is_subsequence.hpp"

namespace cppbase
{

 //! Compute if s is a subsequence of t
 bool isSubsequence(std::string s,  std::string t)
{
    if (s.length() == 0) return true;

    int ptr = 0;
    for(int i = 0; i < t.length(); i++)
    {
        if (t[i] == s[ptr])
        {
            ptr++;
            if (ptr == s.length()) return true;
        } 
    }

    return false;

}

} // namespace cppbase
