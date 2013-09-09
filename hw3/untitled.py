import numpy as np

#a=np.matrix('4 2 1 -1; 1 5 -2 3; 4 4 4 0; -1 6 2 -5')
#b=np.matrix('-1 0 0 0; 0 2 0 0; 0 0 2,0; 0,0,0,3')

a=np.array([[3,4],[2,1]])
b=np.array([[1],[0]])

x = np.linalg.solve(a, b)
print x

