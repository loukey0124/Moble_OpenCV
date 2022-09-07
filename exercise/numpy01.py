from array import array
import numpy as np

arr = np.arange(27)
tr = arr.reshape(3,3,3)
print(tr)
print(tr.transpose())
print(tr.transpose(1,0,2))