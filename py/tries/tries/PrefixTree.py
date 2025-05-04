## === Preface ===

"""

## Implementing a trie (prefix-tree) is a tree data structure for string processing problems.

For use in locating records stored within a low-speed memory medium
where they are identifiable by a key word or words of 
variable length on a machine not equipped to accomplish this automatically

### Also known as a digital tree or prefix tree.

A tree is abstraction data type that represents an upside-down tree from 
the view of the user of the data. A search tree is used for implementing
a dictionary or associative array, algorithm uses the key from the 
key–value pair to find a location, and then the application stores the 
entire key–value pair at that particular location. A trie is a specialized
search tree used to store and retrieve strings from a dictionary/associative array.

- Tries offer advantages over Hash Tables due to prefix-based organization
- Tries can be adapted to work with any ordered sequence
- However, if storing ordered sequences is all that is required then

### Information derived from this lecture and paper
 - https://algs4.cs.princeton.edu/lectures/keynote/52Tries.pdf
 - File Searching Using Variable Length Keys by RENE DE LA BRIANDAIS

## Tries, from retrieval, but pronounced 'try'

- Store character in nodes (not keys).
- Each node has 'R' children, one for each possible character.
    (for now, we do not draw null links)

#### Now we have an R-way Trie, since we'll need references to 'R' nodes

## Search in a Trie

Follow links corresponding to each character in the key.

- Search hit: node where search ends has a non-null value.
- Search miss: reach null link or node where search ends null value

## Trie performance

- Search hit. Need to examine all 'L' characters for equality
- Search miss.
    - Could have mismatch on first character.
    - Typical case: examine only a few characters (sublinear).
- Space. 'R' null links at each leaf

(but sublinear space possible if many short strings share common prefixes)

- Bottom line. Fast search hit and even faster search miss, but wastes space

## Deletion in an R-way Trie

To delete a key-value pair:

- Find the node corresponding to key and set value to null.
- If node has null value and all null links, remove that node (and recur).

#  BORING VARIATION 

###  Challenge. Use less memory, e.g., 65,536-way trie for Unicode!


# Ternary search Tries

- Store characters and values in nodes (not keys).
- Each node has 3 children: smaller(left), equal(middle), larger(right)

## Search in a Ternary search Trie

Follow links corresponding to each character in the key.

 - If less, take left link; if greater take right link.
 - If equal, take the middle link and move to the next key character.

## TST performance

- Bottom line. TST is as fast as hashing (for string keys), space efficient
"""

## === Warmup ===

"""
Suppose you're given an array of strings (dictionary), as for string processing.
But now you want to infer what the longest common prefix (pattern) amongst the strings,
otherwise return an empty string if there is no common prefix.

#### e.g. strings = ["purple","pug","pussycat"], is there a common prefix?  yes -> "pu"


https://neetcode.io/solutions/longest-common-prefix
"""