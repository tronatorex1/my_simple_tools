# These are a few examples on how to use Numpy 
#

import numpy as np

# 1 Creating 1d and 2d arrays
a = np.array([1,2,3], dtype='int8')
b = np.array([[4,5],[6,7]])

# 2 Checking stats pf these previous objects
a.ndim
b.ndim

a.shape
b.shape

a.dtype
b.dtype

a.nbytes
b.nbytes

# 3 Operating arithmetically with simple arrays
#   If not using numpy but list, direct multiplication is not allowed
x = a * a
x

# 4 Use slicing as you would with a List (1d, 2d or 3d)
b[:,1]

# 5 To initialize a new array 
shape = (2,3) # must be a tuple
c = np.zeros(shape, dtype='int32')
c

fixed_value = 999
d = np.full(shape, fixed_value)
d

np.random.rand(4,2)

np.random.random_sample(b.shape) # uses the b matrix shape to create a equally dim object with random numbers


# 6 Formating a complex matrix
output = np.zeros((7,7))
output
z = np.ones((5, 5))
z[2, 2] = 5
z
output[1:-1, 1:-1] = z
output

# 7 OPerations with matrices and series
# Maths
a + a

# Algebra
e = np.identity(3)
np.linalg.det(e)
#   use: https://numpy.org/doc/stable/reference/routines.linalg.html

# Statistics
f = np.array([[1,2,3,4],[0,-1,5,99]])
f
np.min(f)
np.max(f, axis=1)
np.average(f)
np.mean(f)

# 8 Stacking
g = np.array([1,2,3,4,5,6,7])
h = np.full(7, 0)
g, h
np.vstack((g,h))
np.hstack((g,h))

# 9 Loading CSV data from test files
file = np.genfromtxt('file.txt', delimiter=',')
file # float is the Numpy default format or dtype
# cast it to int8 from float
file = file.astype('int8')
file

# If: boolean and other checks
file > 5 # this tells if conditions applies using boolean values
file[file > 5] # this prints out only the values based upon condition, not booleans
np.any(file > 5 , axis=0) # output in boolean as well
(~(file > 4) & (file < 2)) # ~ means not (!)
