import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
res=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

rows=0
while(rows < len(arr)):
    i=len(arr)-1
    j=0
    while(i >= 0):
        res[rows][j]=arr[i][rows]
        j+=1 
        i-=1
    rows+=1
print(res)

