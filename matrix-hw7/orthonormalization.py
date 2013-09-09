from math import sqrt
from matutil import coldict2mat
from orthogonalization import orthogonalize, aug_orthogonalize
from vec import Vec
from vecutil import list2vec



def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    L1 = orthogonalize(L)
    L2 = []
    for i in L1:
        temp = 0
        for j in i.D:
            temp += i[j] ** 2
        L2.append(temp)
    return [L1[i] / sqrt(L2[i]) for i in range(len(L1))]

def adjust(v, multipliers):
    assert set(range(len(multipliers))) == v.D
    w = Vec(v.D, {})
    for i in range(len(v.D)):
        w[i] = multipliers[i]*v[i]
    return w

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    L1, L2 = aug_orthogonalize(L)
    L3 = []
    for i in L1:
        temp = 0
        for j in i.D:
            temp += i[j] ** 2
        L3.append(temp)
    L3 = [sqrt(i) for i in L3]
    Qlist = orthonormalize(L)
    Rlist = [adjust(L2[i], L3) for i in range(len(L2))]
    return Qlist, Rlist