# === Generic Subsequence Functions ===

def isSubsequence(s: str, t: str) -> bool:
    """
    This function is given two strings, s and t, return true if s is 
    a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the
    original string by deleting some (or none) of the characters without
    disturbing the relative positions of the remaining characters.
    (i.e. "ace" is a subsequence of "abcde" while "aec" is not)

    Args:
    s -> String
    t -> String


    Returns -> Boolean

    """

    if not s: return True
    
    ptr = 0 # one pointer (s string iter)
    for chr in t: # two pointer (t string iter)
        if chr == s[ptr]: # if pointer two matches value at index (in s string iter)
            ptr+=1 # increment pointer one
            if ptr == len(s): # if pointer one matches the last character in string s
                return True
    return False

# === Analysis of Data Structures, Algorithms, and Approaches ===
'''
- Big O is a way to categorize your algos time or memory requirements based on input
- it is not meant to be an exact measurement
- growth is with respect to input

m, for length of string t
Time:O(m) Space:O(1)

'''