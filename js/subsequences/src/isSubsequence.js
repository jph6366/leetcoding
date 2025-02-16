// === Generic Subsequence Functions ===
/**
 * This function is given two strings, s and t, return true if s is
 * a subsequence of t, or false otherwise.
 * 
 * A subsequence of a string is a new string that is formed from the
 * original string by deleting some (or none) of the characters without
 * disturbing the relative positions of the remaining characters.
 * (i.e. "ace" is a subsequence of "abcde" while "aec" is not)
 * @
 * @param {string} s
 * @param {string} t
 * 
 * @returns {boolean}
 *  */ 
export default function isSubsequence(s, t) {
    if (s.length === 0) return true; // if s is empty then subsequence is an empty list which should always be a subsequence of any given string

    let ptr = 0;
    for (let chr of t) {
        if (chr === s[ptr]) {
            ptr++;
            if (ptr === s.length) return true;
        }
    }

    return false;
}

