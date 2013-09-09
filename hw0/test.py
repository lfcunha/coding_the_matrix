__author__ = 'luiscunha'


def myFilter(L, num):
    return [x for x in L if x%num!=0]



#print(myFilter([1,2,4,5,7],2))



def myLists(L):
    a=[]
    for i in range(len(L)):
        b= list(range(1, L[i]+1))
        a.append(b)
    return a

#print(myLists([1, 2, 4]))

def myFunctionComposition(f, g):
    return [{a:g[a]} for a in (f[a] for a in f.keys())]




f = {0:'a', 1:'b'}
g = {'a':'apple', 'b':'banana'}

print(myFunctionComposition(f,g))