import numpy as np
Z = np.array([1,2,3,4,5])
nz = 4
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0)