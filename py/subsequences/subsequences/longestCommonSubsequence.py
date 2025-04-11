# === Jump to Thought Process ===
"""
### Interviewer: 
 Given two strings text1 and text2, 
 return the length of their longest common subsequence. 
 If there is no common subsequence, return 0.

### Interviewee:
Let parse the problem statement, 
the main problem is that we are matching two strings up
and returning a value that is derived from matching procedure(s).

#### Pragmatism: 
allow us remove the highest level abstraction, the subsequence.

Given two strings find their longest common _

 - find a matching condition
 - compare all possible combinations to find the longest
 - the matching condition comparator evaluates common properties between two strings

Now lets add our subsequence into solution as a 'first class citizen' and determine if they need structure

 - identify => environment => data => procedure

    ### identify

    1. subsequence of a string, a substring that can be created by removing any amount of character.
    2. common subsequence between two strings; requires use of time to iterate through two strings and space to find common characters between two strings.
    3. longest common subsequence; requires use of time to evaluate longest value and space to store evaluation.

    ### environment: 
    
    python => generic function

    ### data:

    O(m*n) for strings m and n

    ### procedure:

    iteratively compute result derived from overlapping sub-procedures
 
 
"""


## === Preface ===

"""

## Finding the longest common subsequence of two strings is a string matching problem.

## This is a good problem for using dynamic programming techniques.

## Most information is derived from lecture notes from 1996
 https://ics.uci.edu/~eppstein/161/960229.html

Dynamic programming is an algorithmic paradigm, which is an abstraction higher than
the notion of an algorithm. There are two key attributes that a problem must have 
in order for dynamic programming to be applicable:

 - optimal substructure
 - overlapping sub-problems

 If a problem can be solved by combining optimal solutions to non-overlapping
 sub-problems, then it is called 'Divide and Conquer'. This paradigm breaks 
 down a problem into two or more sub-problems of the same/related type, until
 these become simple enough to be solved directly. The solution to the
 sub-problems are then combined to give a solution to the original problem.

Optimal substructure = finding shortest paths in a recursive manner
e.g. Bellman-Ford Algorithm, Floyd-Warshall Algorithm

Overlapping sub-problems = Top-down approach: memoize the solutions to sub-problems
                            || Bottom-Up approach: iterate sub-problems in a tabular form

Principle of Optimality: 
An optimal policy has the property that whatever the initial state and initial decision are, 
the remaining decisions must constitute an optimal policy with regard to the state resulting 
from the first decision. (See Bellman, 1957, Chap. III.3.)

It writes the "value" of a decision problem at a certain point in time in terms of the payoff
 from some initial choices and the "value" of the remaining decision problem that results from 
 those initial choices.

"""


## === Warm-Up ===
"""
Suppose you're given a short string (pattern) and long string (text), as in the string matching problem.
But now you want to know if the letters of the pattern appear in order (but possibly separated) in the text.
If they do, we say that the pattern is a subsequence of the text.

#### e.g. is "nano" a subsequence of "nematode knowledge"? yes -> NemAtode kNOwledge
we can test this using a finite state machine, corresponding to partial subsequences (prefixes of the pattern).

Finite State Machine (FSM) for matching "nano" in "nematode knowledge"

State transitions:
"other" - any character that doesn't match the current expected character
"n", "a", "n", "o" - characters from the pattern "nano"

"""


"""
#### Can we use this to solve the longest common subsequence, given Strings A & B
  This finite-automata theoretic method gives the longest prefix of String A
  that's a subsequence of B. But the longest common subsequence of A and B is 
  not always a prefix of A.
"""
def subseq(P, T):
    P = iter(P)  # Create an iterator from the pattern string
    for char in T:
        if char == next(P, None):
            try:
                next(P)  # Move to the next character in P
            except StopIteration:
                return True
    return False
## === Purpose ===

# Why might we want to solve the longest common subsequence problem?
"""
 - Molecular Biology, DNA sequenes (genes) can be represented as sequences of four letters ACGT,
   corresponding to four submolecules forming DNA. When Biologist find a new sequences,
   they typically want to know what other subsequences it is most similar to. One way o computing
   how similar two sequences are is to find the length of their longest common subsequence

 - File Comparison, The Unix program "diff" is used to compare two different of the same file, to
   determine what changes have been made to the file. It works by finding a longest common subsequence
   of the lines of the two files; any line in the subsequence has not been changed, so what it displays
   is the remaining set of lines that have changed. In this instance, we should think of each line of a
   file as being a single complicated character in a string.

 - Screen Redisplay, Many text editors like "emacs" display part of a file on the screen, updating the
   screen image as the file is changed. For slow dial-in terminals, these programs want to send the terminal
   as few characters as possible to cause it to update its display correctly. It is possible to view the
   computation of the minimum length sequence of characters needed to update the terminal as being a sort
   of common subsequence problem

 - Hot Module Reload, When you update a module during development, the updated version of that module might
   have significant overlaps with the previous version. Finding the longest common subsequence can help
   identify which parts of the state to preserve, and helps patch only the changed parts instead of tearing
   down and reconstructing the module every hot reload.
    - React HMR uses a similar approach to retain component tree and the state.
"""


# === Recursive Subsequence Search Function ===

def recursive_lcs(A, B):
    """
    this function is given two strings, A and B, and very inefficiently, recursively
    returns the length of longest common subsequence
    
    Args:
    A -> String
    B -> String

    Returns -> Number
    """
    if not A or not B:
        return 0
    elif A[0] == B[0]:
        return 1 + recursive_lcs(A[1:], B[1:])
    else:
        return max(recursive_lcs(A[1:],B), recursive_lcs(A,B[1:]))
# The time bounds are binomial coefficients, which (if m=n) are close to 2^n


# === Recursive Subsequence Search w/ Indices Function ===

A = ""
B = ""

def lcs_length(AA, BB):
    global A, B
    A, B = AA, BB
    return subproblem(0, 0)

def subproblem(i, j):
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + subproblem(i + 1, j + 1)
    else:
        return max(subproblem(i + 1, j), subproblem(i, j + 1))


# === Recursive Subsequence Search w/ Memoization Function ===

A = ""
B = ""
L = []

def memoize_lcs_length(AA, BB):
    global A, B, L
    A, B = AA, BB
    m, n = len(A), len(B)
    L = [[-1 for _ in range(n+1)] for _ in range(m+1)] 
    return memoize_subproblem(0, 0)

def memoize_subproblem(i, j):
    if L[i][j] < 0:
        if i == len(A) or j == len(B):
            L[i][j] = 0
        elif A[i] == B[j]:
            L[i][j] = 1 + memoize_subproblem(i+1, j+1)
        else:
            L[i][j] = max(memoize_subproblem(i+1, j), memoize_subproblem(i, j+1))
    return L[i][j]


# === Iterative Subsequence Search w/ Tabulation (Bottom-Up Dynamic Programming) ===

"""
iterative (because it uses nested loops instead of recursion) 
or bottom up (because the order we fill in the array is from 
smaller simpler subproblems to bigger more complicated ones)
"""
def iterative_lcs_length(A, B):
    m, n = len(A), len(B)
    L = [[0 for _ in range(n+1)] for _ in range(m+1)] 


    for i in range(m - 1, -1, -1): # botttom right to top left
        for j in range(n - 1, -1, -1):
            if A[i] == B[j]:L[i][j] = 1 + L[i+1][j+1] # saving work by not repeating subproblem computations
            else:L[i][j] = max(L[i+1][j], L[i][j+1])
    return L[0][0]

"""
One disadvantage over memoizing is that this fills in the entire array
 even when it might be possible to solve the problem by looking at only
   a fraction of the array's cells.
"""

# === Space-Efficient Subsequence Search  ===

"""
One disadvantage of the dynamic programming methods we've described, 
compared to the original recursion, is that they use a lot of space: O(mn) for the array L (the recursion only uses O(n+m)). 

But the iterative version can be easily modified to use less space -- 
the observation is that once we've computed row i of array L, we no longer need the values in row i+1.

In 1975, Dan Hirschberg showed how to find not just the length, 
but the longest common subsequence itself, in linear space and O(mn) time.
The idea is as above to use one-dimensional arrays X and Y to store the rows
 of the larger two dimensional array L. 
 
 But Hirschberg's method treats the 
 middle row of array L specially: 


 - for all i<m/2, he stores along with the numbers in X and Y the place where some path (corresponding to a subsequence with that many characters) crosses the middle row. 

  - These crossing places can be updated along with the array values, by copying them from X[j+1], Y[j], or Y[j+1] as appropriate.

"""

def space_efficient_lcs_length(A, B):
    m, n = len(A), len(B)
    # Ensure A is the shorter string to minimize space (O(min(m, n)))
    if m > n:
        A, B = B, A
        m, n = n, m
    
    # Initialize two arrays of size n+1
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    
    for i in range(m - 1, -1, -1):  # Iterate from m-1 to 0
        for j in range(n - 1, -1, -1):  # Iterate from n-1 to 0
            if A[i] == B[j]:
                X[j] = 1 + Y[j + 1]
            else:
                X[j] = max(Y[j], X[j + 1])
        
        # Copy X to Y for the next iteration
        Y = X.copy()
    
    return X[0]

"""
Then when the algorithm above has finished with the LCS length in X[0], Hirschberg finds the corresponding crossing place (m/2,k). 

He then solves recursively two LCS problems, one for A[0..m/2-1] and B[0..k-1] and one for A[m/2..m] and B[k..n]. The longest common subsequence is the concatenation of the sequences found by these two recursive calls.

It is not hard to see that this method uses linear space. What about time complexity? This is a recursive algorithm, with a time recurrence

    T(m,n) = O(mn) + T(m/2,k) + T(m/2,n-k)
You can think of this as sort of like quicksort -- we're breaking both strings into parts. 

But unlike quicksort it doesn't matter that the second string can be broken unequally. 

No matter what k is, the recurrence solves to O(mn). The easiest way to see this is to think about what it's doing in the array L. 

The main part of the algorithm visits the whole array, then the two calls visit two subarrays, one above and left of (m/2,k) and the other below and to the right. 

No matter what k is, the total size of these two subarrays is roughly mn/2. So instead we can write a simplified recurrence

    T(mn) = O(mn) + T(mn/2)
    
which solves to O(mn) time total.

"""
