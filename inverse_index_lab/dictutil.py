## Task 2
def dict2list(dct, keylist):
    return [dct[z] for z in keylist]


def list2dict(L, keylist):
    return {z:y for (y, z) in (x for x in zip(L, keylist))}




## Task 3
def listrange2dict(L):
    """

    :param L:
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    return list2dict(L, range(len(L)))



