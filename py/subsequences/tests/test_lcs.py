from subsequences.longestCommonSubsequence import recursive_lcs, lcs_length, memoize_lcs_length

def test_level_1():

    assert recursive_lcs("a", "a") == 1
    assert recursive_lcs("abcde", "ace") == 3
    assert recursive_lcs("abc", "abc") == 3
    assert recursive_lcs("abc", "def") == 0
    assert recursive_lcs("oxcpqrsvwf", "shmtulqrypy") == 2



def test_level_2(): 

    assert lcs_length("a", "a") == 1
    assert lcs_length("abcde", "ace") == 3
    assert lcs_length("abc", "abc") == 3
    assert lcs_length("abc", "def") == 0
    assert lcs_length("oxcpqrsvwf", "shmtulqrypy") == 2

def test_level_3(): 

    assert memoize_lcs_length("a", "a") == 1
    assert memoize_lcs_length("abcde", "ace") == 3
    assert memoize_lcs_length("abc", "abc") == 3
    assert memoize_lcs_length("abc", "def") == 0
    assert memoize_lcs_length("oxcpqrsvwf", "shmtulqrypy") == 2