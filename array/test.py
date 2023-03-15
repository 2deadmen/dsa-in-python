import numpy as np

arr = np.array([[1,2,3],[1,2,3]])
new=np.delete(arr,0,axis=1)
print(new)