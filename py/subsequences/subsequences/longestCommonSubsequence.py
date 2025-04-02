## === Jump to Thought Process ===
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

### Pseudo-Code ===>

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

