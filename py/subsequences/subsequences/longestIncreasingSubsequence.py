# === Generic Subsequence Search Function ===

from typing import List

def longestIncreasingSubsequence(nums: List[int]) -> bool:
    """
    This function is given an integer array nums, return the length of
    the longest strictly increasing subsequence.

    The longest strictly increasing subsequence of an array of integers 
    is formed from the original and by deleting some or none of the 
    elements, without changing the relative order of the remaining 
    characters.
    (i.e. [1,2,3,7] is the longest increasing subsequence of [9,1,4,2,3,3,7])

    Args:
    nums -> Array<Integer>


    Returns -> Number

    """
    # subsequence is basically subarray without a requirement searching for contiguous order

    # brute force dfs
    # use decision tree to visualize
    # generate every possible subsequence in O(2^n) time and O(n) space 
    # we want to get generate the result starting at every index
    # nums: [1,2,4,3] => returns {    
    # subsequenceLengthAtIndex[0] = 3,  
    # subsequenceLengthAtIndex[1] = 2, 
    # subsequenceLengthAtIndex[2] = 1, 
    # subsequenceLengthAtIndex[3] = 1    
    # }

    # dfs with caching
    # iterates in O(n^2) time and O(n) space
    # nums: [1,2,4,3]
    # subsequenceLengthAtIndex[3] = 1
    # subsequenceLengthAtIndex[2] = max(1, 1+LIS[3]) ? is nums[2] < nums[3] -> not increasing -> then returns 1
    # subsequenceLengthAtIndex[1] = max(1, 1+LIS[2], 1+LIS[3]) returns 2
    # subsequenceLengthAtIndex[0] = max(1, 1+LIS[1], 1+LIS[2], 1+LIS[3]) returns 3

    LIS = [1] * len(nums)

    # Bottom-Up Dynamic Programming
    for i in range(len(nums) - 1, -1, -1): # starts at last index and goes all the way to zero
        for j in range(i+1, len(nums)): # iterate through every subsequence that comes after index i
            if nums[i] < nums[j]: # j comes after so check if its increasing
                LIS[i] = max(LIS[i], 1+LIS[j]) # update longest increasing subsequence at index i and set it to the 
    return max(LIS) # max of a list in O(n) time




# === Analysis of Data Structures, Algorithms, and Approaches ===
'''
- Big O is a way to categorize your algos time or memory requirements based on input
- it is not meant to be an exact measurement
- growth is with respect to input

m, for length of string t
Time:O(m) Space:O(1)

'''