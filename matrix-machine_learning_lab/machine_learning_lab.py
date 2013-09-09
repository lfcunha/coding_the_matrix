from mat import *
from vec import *
from cancer_data import *
import random as rd
from decimal import Decimal

A, b=read_unclassified_data('train.data');


## Task 1 ##
def signum(u):
    '''

    :param u:
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1

    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''

    a=Vec(u.D,[{key:(-1,1)[u.f[key]>=0] for key in u.f}][0])



    b=[x for x in u.D]
    for x in range(len(b)):
        if (b[x] not in u.f.keys()):
            a.f[b[x]]=1


    return a


#Vec[u.D, {key:0 for key in u.f}]

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''

    a = signum(A*w)
    return float(len([x for x in b.D if b[x] != a[x]])/len(b.D))




## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    return ( A * w - b) * ( A * w - b)
#print(loss(A, b, w))

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return 2*(( A * w - b)*A)

#print(find_grad(A, b, w))


## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w-sigma*find_grad(A,b,w)

