from array import *
arr=array('i',[1,2,3,5,6])
for i in arr:
    for j in arr:
        if i+j==5:
            print(i,j)