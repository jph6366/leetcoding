

# === Recursive Integer Break Function ===

def recursive_intbreak_maximum(n):
    """
    this function is given an integer n, 
    breaks it into the sum of k positive integers, 
    where k >= 2, and maximize the product of those integers.
    Return the maximum product you can get.
    
    Args:
    n -> Number

    Returns -> Number
    """

    def subproblem(n, idx):
        if n == 0 or idx == 0:
            return 1
        if idx > n:
            return subproblem(n, idx - 1)
        return max((idx * subproblem(n-idx, idx), subproblem(n, idx-1)))
    
    return subproblem(n, n-1)

# Time Complexity: O(n), the recursive calls.
# Auxiliary Space: O(n), recursive stack space

# === Rule of Three Integer Break Function ===

def rofthree_intbreak_maximum(n):
    """
    this function is given an integer n, 
    breaks it into the sum of k positive integers, 
    maxima obtained by repeatedly cutting parts of size 3 while size is greater than 4,
    keeping the last part as size of 2 or 3 or 4.
    Return the maximum product you can get.
    
    Args:
    n -> Number

    Returns -> Number
    """
    if n == 2 or n == 3:
        return (n - 1)
    
    res = 1
    while(n > 4):

        n-=3
        res*=3
    return n*res


# Time Complexity: O(n)
# Auxiliary Space: O(1)


# === Computing Powers by Repeated Squaring Integer Break Function ===

# https://planetmath.org/computingpowersbyrepeatedsquaring

def power_intbreak_maximum(n):
    """
    this function is given an integer n, 
    breaks it into the sum of k positive integers, 
    maxima obtained by repeatedly cutting parts of size 3 while size is greater than 4,
    keeping the last part as size of 2 or 3 or 4.
    Return the maximum product you can get.
    
    Args:
    n -> Number

    Returns -> Number
    """

    # method return x^a in log(a) tim
    def power(x, a):

        res = 1
        while (a):
            if (a & 1):
                res = res * x
            x = x * x
            a >>= 1

        return res
    
    if n == 2: return 1
    if n == 3: return 2

    mP = 0
    if n % 3 == 0:
        mP = power(3, int(n/3))
        return mP
    elif n % 3 == 1:
        mP = 2 * 2 * power(3, int(n/3) - 1)
        return mP
    elif n % 3 == 2:
        mP = 2 * power(3, int(n/3))
        return mP

# Time Complexity: O(log n)
# Auxiliary Space: O(1)