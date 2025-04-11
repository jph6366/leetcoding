from subsequences.longestCommonSubsequence import iterative_lcs_length, recursive_lcs, lcs_length, memoize_lcs_length, space_efficient_lcs_length

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

def test_level_4(): 

    assert iterative_lcs_length("a", "a") == 1
    assert iterative_lcs_length("abcde", "ace") == 3
    assert iterative_lcs_length("abc", "abc") == 3
    assert iterative_lcs_length("abc", "def") == 0
    assert iterative_lcs_length("oxcpqrsvwf", "shmtulqrypy") == 2

def test_level_5(): 

    assert space_efficient_lcs_length("a", "a") == 1
    assert space_efficient_lcs_length("abcde", "ace") == 3
    assert space_efficient_lcs_length("abc", "abc") == 3
    assert space_efficient_lcs_length("abc", "def") == 0
    assert space_efficient_lcs_length("oxcpqrsvwf", "shmtulqrypy") == 2