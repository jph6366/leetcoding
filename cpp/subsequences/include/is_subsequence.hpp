
 #pragma once
#include <string>

 namespace cppbase
 {
 
 //! Compute if s is a subsequence of t
 /*!
  * This function is given two strings, s and t, return true if s is
  * a subsequence of t, or false otherwise.
  * 
  * A subsequence of a string is a new string that is formed from the
  * original string by deleting some (or none) of the characters without
  * disturbing the relative positions of the remaining characters.
  * (i.e. "ace" is a subsequence of "abcde" while "aec" is not)
  *
  * @param[in]  s  the string to search for as a subsequence
  * @param[in]  t  the original string that will possibly form the given subsequence by deleting some characters
  * @return                    boolean indicating if s is a subsequence of t
  */
 bool isSubsequence(std::string s, std::string t);
 
 } // namespace cppbase