#!/usr/bin/env python3

# === Thought Process ===

"""
### Interviewer:
There are n houses in a village.
We want to supply water for all the houses by building wells and laying pipes.

For each house i,
we can either build a well inside it directly with cost wells[i - 1]
(note the -1 due to 0-indexing),
or pipe in water from another well to it.
The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe.
Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.


"""

## === Preface ===
"""
## Finding the minimum total cost is a st-connectivity problem

## This problem requires using a undirected edge-weighted graph.
### More specifically, modeling the water supply graph using a minimum spanning tree/forest of a weighted graph

#### In DFS of an undirected graph, we get only tree and back edges
 - Tree edge: in the depth-first forest, found by exploring (u,v)
 - Back edge: (u,v), where u is a descendant of v (in the depth-first tree)

#### Finding the minimum spanning tree:
-  Find a key property of the MST that lets us be sure that some edge part of it, and use this property to build up the MST one edge at a time.

#### Kruskal's Algorithm
- in 1956, Joseph Kruskal published his work for computing the minimal spanning forest of a undirected edge-weighted graph.

    1. sort the edges of G in increasing order by length
    2. keep a subgraph S of G, initally empty
    3. for each edge e in sorted order
        1. if the endpoints of e are disconnected in S
           - add e to S
    4. return S

- this is a greedy algorithm, because it chooses at each step the cheapest edge to add to S
   - the greedy idea only works in Kruskal's algorithm because of the MST's key property
"""

## === Warm-Up ===
"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

"""

class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res
"""
 time Θ(n^2 log(n))

 space Θ(n^2)
"""

## === Kruskal's Algorithm ===

class Solution:
    def minCostToSupplyWater(
            self, n: int, wells, pipes) -> int:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i, w in enumerate(wells, 1):
            pipes.append([0, i, w])
        pipes.sort(key=lambda x: x[2])
        p = list(range(n + 1))
        ans = 0
        for a, b, c in pipes:
            pa, pb = find(a), find(b)
            if pa != pb:
                p[pa] = pb
                n -= 1
                ans += c
                if n == 0:
                    return ans


## === Evaluation ===
## where E is the number of pipes and V is number of wells
##
##  time Θ(E*log(E) + V)
##  space Θ(V + E)
##
