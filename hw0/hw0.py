# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    return [x for x in L if x%num!=0]



## Problem 2
def myLists(L):
    a=[]
    for i in range(len(L)):
        b= list(range(1, L[i]+1))
        a.append(b)
    return a



## Problem 3
def myFunctionComposition(f, g):
    #return [{a:g[a]} for a in (f[a] for a in f.keys())]
    return dict([[a,g[b]] for (a,b) in  (a for a in (a for a in (zip((a for a in f.keys()), (f[a] for a in f.keys())))))])

#f = {0:'a', 1:'b'}
#g = {'a':'apple', 'b':'banana'}

#print(myFunctionComposition(f,g))


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5 + 3j)
complex_addition_b = (1j)
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    a=0
    for i in range(len(L)):
        a+=L[i]
    return a



## Problem 7
def myProduct(L):
    a=1
    for i in range(len(L)):
        a=a*L[i]
    return a




## Problem 8
def myMin(L):
    a=L[0];
    for i in range(len(L)):
        if L[i]<a:
            a=L[i]
    return a
#print(myMin([10, 6, 2, 9, 3, 6, 8]))


## Problem 9
def myConcat(L):
    a=''
    for i in range(len(L)):
        a+=L[i]
    return a

#print(myConcat(['a', 'b']))


import itertools
## Problem 10
def myUnion(L):
    def a(*args):
        return set(itertools.chain.from_iterable(args))
    return a(*L)
L=[set(['a', 'b']), set(['b', 'c']), set(['a', 'b', 'x'])]
#L=[]
#print(L)
print(myUnion([L]))


