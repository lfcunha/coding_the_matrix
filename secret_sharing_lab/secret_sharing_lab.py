# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec
from itertools import combinations
from independence import is_independent
rand = random.SystemRandom()
## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        secret = [ randGF2() for i in range(6) ]
        secret = list2vec(secret)
        print(secret)
        if a0 * secret == s and b0 * secret == t:
            return secret


def pick_known_vectors(a, b):
    all = [ (a,b),None,None,None,None ]
    while True:
        for i in range(1,5):
            all[i] = (list2vec([ randGF2() for i in range(6) ]),
                      list2vec([ randGF2() for i in range(6) ]))
        ok = True
        for x,y,z in combinations(range(5), 3):
            L = [ all[x][0], all[x][1], all[y][0], all[y][1], all[z][0], all[z][1] ]
            if not is_independent(L):
                ok = False
                break
        if ok:
            return all

known = pick_known_vectors(a0, b0)
## Problem 2
# Give each vector as a Vec instance
secret_a0 = known[0][0]
secret_b0 = known[0][1]
secret_a1 = known[1][0]
secret_b1 = known[1][1]
secret_a2 = known[2][0]
secret_b2 = known[2][1]
secret_a3 = known[3][0]
secret_b3 = known[3][1]
secret_a4 = known[4][0]
secret_b4 = known[4][1]

