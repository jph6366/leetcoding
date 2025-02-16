#include <catch2/catch_test_macros.hpp>

#include "../include/is_subsequence.hpp"

namespace cppbase
{
namespace tests
{

TEST_CASE("Check if a string is a subsequence of another", "[isSubsequence]")
{
    REQUIRE(isSubsequence("", "") == true);  // Empty string is a subsequence of another empty string
    REQUIRE(isSubsequence("abc", "ahbgdc") == true);  // "abc" is a subsequence of "ahbgdc"
    REQUIRE(isSubsequence("axc", "ahbgdc") == false); // "axc" is not a subsequence of "ahbgdc"
}

} // namespace tests
} // namespace cppbase
