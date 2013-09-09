# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from vecutil import *
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    if len(A) == 0:
        return False
    if len(A[0]) == 0:
        return False
    max_i = len(A)
    max_j = len(A[0])
    i = 0
    j = 0
    while i < max_i and j < max_j:
        for zi in range(i + 1, max_i):
            if A[zi][j] != 0:
                return False
        if A[i][j] != 0:
            i = i + 1
        j = j + 1
    return True



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1, 0, 3, 0]
echelon_form_vec_b = [-3, 0, -2, 3]
echelon_form_vec_c = [-5, 0, 2, 0, 2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]



def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
D = {'A','B','C','D','E'}
U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
b_list = [one,0,one]
cols = ['A', 'B', 'C', 'D', 'E']
echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    x = zero_vec(set(label_list))
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        c = next((i for i in label_list if row[i] != 0), None)
        if c:
            x[c] = (b[j] - x*row)/row[c]
    return x




## Problem 6
M=coldict2mat({ 'a':list2vec([one,one,one,one]), 'b':list2vec([0,one,0,0]),
                'c':list2vec([0,0,one,one]), 'd':list2vec([0,0,0,one]) })
g = Vec({'a','b','c','d'},{ 'a':one, 'c':one})
U=coldict2mat({ 'A':list2vec([one,0,0,0]), 'B':list2vec([one,one,0,0]),
                'C':list2vec([0,0,one,0]), 'D':list2vec([one,0,0,one]) })
U_rows_dict = mat2rowdict(U)
rowlist = [U_rows_dict[i] for i in U_rows_dict]    # Provide as a list of Vec instances
label_list = sorted(U.D[1]) # Provide as a list
Mg = M*g
b = [ Mg[x] for x in Mg.D ]          # Provide as a list


## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}


def project_along(b,a):
    ''' give the projection of b along a. b and a are lists, returns a list '''
    b = list2vec(b)
    a = list2vec(a)
    x = ((b*a)/(a*a) if a*a > 1E-20 else 0)*a
    return [x[i] for i in x.D]

def ortho(b,a):
    x = project_along(b,a)
    return [ bi - xi for bi, xi in zip(b,x) ]
## Problem 9
# Write each vector as a list
closest_vector_1 = project_along([2,3], [1,2])
closest_vector_2 = project_along([1.414,1,1.732],[0,1,0])
closest_vector_3 = project_along([7,2,5,0],[-3,-2,-1,4])

print(closest_vector_1)
print(closest_vector_2)
print(closest_vector_3)


## Problem 10
# Write each vector as a list

project_onto_1 = project_along([2,1],[3,0])
projection_orthogonal_1 = ortho([2,1],[3,0])

project_onto_2 = project_along([1,1,4],[1,2,-1])
projection_orthogonal_2 = ortho([1,1,4],[1,2,-1])

project_onto_3 = project_along([1,1,4],[3,3,12])
projection_orthogonal_3 = ortho([1,1,4],[3,3,12])


## Problem 11
norm1 = sum(x*x for x in [2,2,1])**0.5
norm2 = sum(x*x for x in [2**0.5, 3**0.5, 5**0.5, 6**0.5])**0.5
norm3 = 1

