from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon
import independence
import math
## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return (0 if i%2==0 else one)



## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, { f:one for f, e in factors if int2GF2(e) == one })

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = []
    rowlist = []
    x = intsqrt(N)+2
    while len(roots) < len(primeset)+1:
        factors = dumb_factor(x*x-N, primeset)
        if factors:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))
        x += 1
    return roots, rowlist


## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input:
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [ roots[i] for i in v.f if v[i]==one ]
    a = prod(alist)
    c = prod(x*x-N for x in alist)
    b = intsqrt(c)
    if b*b == c:
        return a, b
    return None

## Task 5
def factor_woojoo(N, primeset):
    roots, rowlist = find_candidates(N, primeset)
    M = echelon.transformation_rows(rowlist, sorted(primeset, reverse=True))
    rank = independence.rank(rowlist)
    for i in range(len(M)-1,rank-1,-1):
        a, b = find_a_and_b(M[i], roots, N)
        ans = gcd(a-b, N)
        if ans > 1:
            return ans
    return None

primeset=primes(10000)
smallest_nontrivial_divisor_of_2461799993978700679 = factor_woojoo(2461799993978700679,primeset)