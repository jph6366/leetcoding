#!/usr/bin/env python3
#
#
from collections import deque
# === Thought Process ===

"""
### Interviewer:
You are given an array prerequisites
where prerequisites[i] = [a, b]
indicates that you must take course b first
if you want to take course a.

The pair [0, 1], indicates that must take course 1
before taking course 0.

There are a total of numCourses courses you are required to take,
labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses,
otherwise return false.

"""

## === Preface ===

"""
## Validating this course schedule is a traversal problem.

## This is a good problem for using a directed acyclic graph.
### More specificly, modeling the course schedule evaluation using a partial order.

#### Characterizing a DAG:
- A directed graph, G, is acyclic if DFS of G yields no back edges

#### "Sorting" a DAG:
Topological sorting is a linear ordering of vertices of G
such that for every directed edge (u, v), from vertex u to vertex v, u comes before v in the ordering.

- a topological ordering is just a valid sequence for the tasks
- a topological sort is a graph traversal in which each node v is visited only after all its dependencies are visited.

A graph has a topological ordering/sorting if and only if it is a directed acyclic graph.
There are three mathematical properties to a directed acyclic graph, a directed graph with no directed cycles.

- Reachability, refers to general st-connectivity problem for directed graphs, the problem of finding a path from one vertex to another in a graph.
  - two vertices u and v are ordered as u <= v exactly where there exists a directed path from u to v in the DAG.

- Transitive closure, refers to determine the connected components of directed graphs, constructing a data structure that makes it possible to answer reachability questions.
  - the adjancency relation of DAG is the reachability relation of the DAG and strict partial order
    - strict partial order is a homogeneous relation < on a set P that is irreflexive, asymmetric, and transitive:

    1. Irreflexivity: no element is related to itself
    2. Asymmetry: the binary relation R on set X where for all a,b belonging to X, if as is related to b then b is not related to a
    3. Transitivity: the binary relation R on set X is transitive if, for all elements a, b, c in X, wherever R relates a to b and b to c, then R also relates a to c

- Transitive reduction, refers to a graph that has the fewest edges possible and has the same reachability relation as the original graph
  - The transitive reduction of a finite directed acyclic graph G is unique, and consists of edges of G that form the only path between their endpoints.
    - transitive and reductive properties coincides with a minimum spanning subgraph of the given graph

### Structuring the problem:

A list in topological order has a special property.

Simply expressed: proceeding element to element along any path in the network,
one passes through the list in one direction only.

So as long as the graph of prequisites have no circular dependencies then we can return true.

#### There are two standard representations of graphs

   1. Adjacency List

- Consists of an array that has one list per vertex
- Space for directed graph Θ(|V|+|E|)
- Time querying directed graph Θ(|V|)
- Time for adding an edge or vertex Θ(1)
- Time for removing a vertex from directed graph Θ(|V|+|E|)
- Time for removing an edge from directed graph Θ(|E|)


   2. Adjacency Matrix

- |V| x |V| matrix A, Number vertices from 1 to |V| in some arbitrary manner
- Space for directed graph Θ(|V|^2)
- Time querying directed graph Θ(1)
- Time for adding a vertex Θ(|V|^2)
- Time for adding an edge Θ(1)
- Time for removing a vertex from directed graph Θ(|V|^2)
- Time for removing an edge from directed graph Θ(1)


"""

## == Warm-Up ===

"""
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.



"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
        return False
"""
 time Θ(n)

  space Θ(n)
"""
## === Purpose ===
"""

"""

## === Cycle Detection using DFS ===

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


## === Topological Sort using Kahn's Algorithm ===

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses
