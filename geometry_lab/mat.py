from vec import Vec
from GF2 import one
import vec
#from mat import Mat
def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    if (k in M.f):
        return M.f[k]
    else:
        return 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k]=val


def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    a={}
    for key in A.f:
        if key in B.f :
            a[key]=A.f[key]+B.f[key]
        else:
            a[key]=A.f[key]
    for key in B.f:
        if key not in A.f:
            a[key]=B.f[key]
    return Mat(A.D, a)



def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M"
    a={}
    for key in M.f:
        a[key]=M[key]*alpha
    return Mat(M.D, a)


def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    for key in A.f:
        if A[key]!=B[key]:
            return False
    for key in B.f:
        if B[key]!=A[key]:
            return False
    return True

def transpose(M):
    "Returns the transpose of M"

    return Mat((M.D[1],M.D[0]), {(q,p):v for (p,q),v in M.f.items()})

def vector_matrix_mul(v, A):
    "Returns the product of vector v and matrix M"
    assert A.D[0] == v.D
    #
    # a=[x for x in [x for x in [[v[y]*M[(y,x)] for x in [M.f] for x in M.D[1]] for y in M.D[0]]]]
    # b=[sum(a) for a in zip(a[0],a[1])]
    # c=[x for x in M.D[1]]
    # return Vec(M.D[1],{c[i]:b[i] for i in range(len(b))})
    a={row:v[row]*Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}
    a=[x for x in a.values()]
    t=a[0]
    for i in range(1,len(a)):
        t=t+a[i]
    return t



def matrix_vector_mul(A, v):

    "Returns the product of matrix M and vector v"
    assert(A.D[1] == v.D)
    a={col:v[col]*Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}
    a=[x for x in a.values()]
    t=a[0]
    for i in range(1,len(a)):
        t=t+a[i]
    return t






def matrix_matrix_mul(A, B):

    #a= {r:Vec(M.D[1], {c:M[r,c] for c in M.D[1]}) for r in M.D[0]}
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]

    M=Mat((A.D[0], B.D[1]), {})
    a={row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}
    b={col:Vec(B.D[0], {row:B[row,col] for row in B.D[0]}) for col in B.D[1]}
    r= [{(z,y):p*w } for (z,p) in a.items() for (y,w) in b.items()]
    for r in r:
        for a in r:
            M[a]=r[a]
    return M
################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"

# v1 = Vec({1, 2}, {1: 3, 2: 4})
# M1 = Mat(({1, 2}, {1, 2, 3}), {(1, 1): 1, (1, 2): 2, (1, 3):3, (2, 1):10, (2, 2): 20, (2, 3): 30})
# print(Mat(({1, 2}, {1, 2, 3}), {(1, 1): 1, (1, 2): 2, (1, 3):3, (2, 1):10, (2, 2): 20, (2, 3): 30}))
# print(vector_matrix_mul(v1,M1))

#N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
#u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
#print(matrix_vector_mul(N1, u1))

# v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
# M1 = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
# print(vector_matrix_mul(v1,M1))

#M = Mat(({0,2,'a'},{'b','c','d'}), {(0,'b'): one, (0, 'c'): one, (2, 'd'): one, ('a','c'):one})
#v = Vec({'b','c','d'}, {'b':one,'d':one})
#print(matrix_vector_mul(M,v))
# v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
# M1 = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
# print(v1*M1)
# print(Vec({1, 2, 3},{1: -8, 2: 2, 3: 0}))

