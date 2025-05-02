// === Generic LCS Functions ===
/**
 * This function is given two strings, s and t, 
 * return the length of their longest common subsequence.
 * If there is no common subsequence, return 0.
 * 
 * A subsequence of a string is a new string that is formed from the
 * original string by deleting some (or none) of the characters without
 * disturbing the relative positions of the remaining characters.
 * (i.e. "ace" is a subsequence of "abcde" while "aec" is not)
 * @
 * @param {string} s
 * @param {string} t
 * 
 * @returns {number}
 *  */ 


export function naive_LCS(s,t) {
    if(s.length==0 || t.length==0) {
        return 0;
    }
    if(s[0] == t[0]){
        return 1 + naive_LCS(s.slice(1), t.slice(1));
    } else {
        return Math.max(naive_LCS(s.slice(1),t),naive_LCS(s,t.slice(1)));
    }
}


export function recursive_LCS(s,t) {

    function subproblem(i,j) {
        if(i == s.length || j == t.length){
            return 0;
        }
        if(s[i] == t[j]) {
            return 1 + subproblem(i+1,j+1);
        } else {
            return Math.max(subproblem(i+1,j), subproblem(i,j+1));
        }
    }
    return subproblem(0,0);
}

export function memoize_LCS(s,t) {
    const m = s.length;
    const n = t.length;
    let cache = Array.from({length: m + 1}, () => Array.from({length: n + 1}).fill(-1));
    function subproblem(i,j) {
        if(cache[i][j] < 0) {
            if(i == m || j == n) {
                cache[i][j] = 0;
            } else if(s[i] == t[j]) {
                cache[i][j] = 1 + subproblem(i+1,j+1);
            } else {
                cache[i][j] = Math.max(subproblem(i+1,j), subproblem(i,j+1));
            }
        }
        return cache[i][j];
    }
    return subproblem(0,0);
}

export function iterative_DP_LCS_len(s,t) {
    const m = s.length;
    const n = t.length;
    let cache = new Array(m + 1).fill(null).map(() => new Array(n + 1).fill(0));
    for(let i = m; i >= 0; i--) {
        for(let j = n; j >= 0; j--) {
            if( i == m || j == n) {
                cache[i][j] = 0;
            } else if(s[i] === t[j]) { // strict equality
                cache[i][j] = 1 + cache[i+1][j+1];
            } else {
                cache[i][j] = Math.max(cache[i+1][j], cache[i][j+1]);
            }
        }
    }
    return cache[0][0];
}


// === SUBJECTIVE VARIATION ===
/**
 * This function is the obvious subjective variation, which is to return the actual realized subsequence
 * values in memory, rather than just the length of the subsequence. We can find the sequence by working 
 * forwards through the array.
 *  */ 


export function iterative_DP_LCS_seq(s,t) {
    const m = s.length;
    const n = t.length;
    let cache = new Array(m + 1).fill(null).map(() => new Array(n + 1).fill(0));
    for(let i = m; i >= 0; i--) { // bottom-right to top left
        for(let j = n; j >= 0; j--) {
            if( i == m || j == n) {
                cache[i][j] = 0;
            } else if(s[i] === t[j]) { // strict equality
                cache[i][j] = 1 + cache[i+1][j+1];
            } else {
                cache[i][j] = Math.max(cache[i+1][j], cache[i][j+1]);
            }
        }
    }
    // return cache[0][0];
    let i = 0;
    let j = 0;
    let LCS = [];
    // We traverse while we are within the bounds of the original strings
    while (i < m && j < n) {
        if (s[i] === t[j]) {
            LCS.push(s[i]);
            i++;
            j++;
        } else if (cache[i + 1][j] > cache[i][j + 1]) {
            i++;
        } else {
            j++;
        }
    }

    return LCS;
}


// // // // // // // // // // // // // // // // // // // // //
//     n  e  m  a  t  o  d  e  _  k  n  o  w  l  e  d  g  e

// e   7  7  6  5  5  5  5  5  4  3  3  3  2  2  2  1  1  1  0
// m   6  6  6  5  5  4  4  4  4  3  3  3  2  2  1  1  1  1  0
// p   5  5  5  5  5  4  4  4  4  3  3  3  2  2  1  1  1  1  0
// t   5  5  5  5  5  4  4  4  4  3  3  3  2  2  1  1  1  1  0
// y   4  4  4  4  4  4  4  4  4  3  3  3  2  2  1  1  1  1  0
// _   4  4  4  4  4  4  4  4  4  3  3  3  2  2  1  1  1  1  0
// b   3  3  3  3  3  3  3  3  3  3  3  3  2  2  1  1  1  1  0
// o   3  3  3  3  3  3  3  3  3  3  3  3  2  2  1  1  1  1  0
// t   3  3  3  3  3  2  2  2  2  2  2  2  2  2  1  1  1  1  0
// t   3  3  3  3  3  2  2  2  2  2  2  2  2  2  1  1  1  1  0
// l   2  2  2  2  2  2  2  2  2  2  2  2  2  2  1  1  1  1  0
// e   1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  0
//     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
// // // // // // // // // // // // // // // // // // // // //



// Let's draw a directed graph, with vertices corresponding to entries in the cache array,
//  and an edge connecting an entry to one it depends on: 
//      either one edge to cache[i+1,j+1] if s[i]=t[j], 
//      or two edges to cache[i+1,j] and cache[i,j+1] otherwise. 
//  Don't draw edges from the bottom right fringe of the array 
//   (since those entries don't depend on any others).
//
//        n e m a t o d e _ k n o w l e d g e

//     e  o-o o-o-o-o-o-o o-o-o-o-o-o-o o-o-o o
//        |  \| | | | |  \| | | | | |  \| |  \|
//     m  o-o-o o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | |  \| | | | | | | | | | | | | | | |
//     p  o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | | | | | | | | | | | | | | | | | | |
//     t  o-o-o-o-o o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | | | |  \| | | | | | | | | | | | | |
//     y  o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | | | | | | | | | | | | | | | | | | |
//     _  o-o-o-o-o-o-o-o-o o-o-o-o-o-o-o-o-o-o
//        | | | | | | | |  \| | | | | | | | | |
//     b  o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | | | | | | | | | | | | | | | | | | |
//     o  o-o-o-o-o-o o-o-o-o-o-o o-o-o-o-o-o-o
//        | | | | |  \| | | | |  \| | | | | | |
//     t  o-o-o-o-o o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | | | |  \| | | | | | | | | | | | | |
//     t  o-o-o-o-o o-o-o-o-o-o-o-o-o-o-o-o-o-o
//        | | | |  \| | | | | | | | | | | | | |
//     l  o-o-o-o-o-o-o-o-o-o-o-o-o-o o-o-o-o-o
//        | | | | | | | | | | | | |  \| | | | |
//     e  o-o o-o-o-o-o-o o-o-o-o-o-o-o o-o-o o
//        |  \| | | | |  \| | | | | |  \| |  \|
//        o o o o o o o o o o o o o o o o o o o

// Then if you look at any path in the graph, the diagonal edges form a subsequence of the two strings. 
// Conversely, if you define the horizontal and vertical edges to have length zero, and the diagonal 
// edges to have length one, the longest common subsequence corresponds to the longest path from the 
// top left corner to one of the bottom right vertices. This graph is acyclic, so we can compute 
// longest paths in time linear in the size of the graph, here O(mn).

// This sort of phenomenon, in which a dynamic programming problem turns out to be equivalent to a 
// shortest or longest path problem, does not always happen with other problems, but it is reasonably 
// common. This idea doesn't really help compute the single longest common subsequence, but can use
// graph-theoretic ideas to find multiple long common subsequences.

// Read more from source material here https://ics.uci.edu/~eppstein/161/960229.html


export function Hirschberg_LCS_len(s,t) {
    let A,B;
    if (s.length <= t.length) {
        A = s;
        B = t;
    } else {
        A = t;
        B = s;
    }

    const n = B.length;
    const m = A.length;

    let X = new Array(n+1).fill(0);
    let Y = new Array(n+1).fill(0);

    for(let i = m; i >= 0; i--) {
        for(let j = n; j >= 0; j--) {
            if (i === m || j === n) {
                X[j] = 0;
            }
            else if(A[i] == B[j]) {
                X[j] = 1 + Y[1+j];
            } else {
                X[j] = Math.max(Y[j], X[j+1]);
            }
        }
        Y = [...X]; // sspread
    }
    return Y[0];
}
