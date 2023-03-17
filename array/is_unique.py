from array import *
arr=array('i',[1,2,3,5,6,1])
flag=True
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            flag=False
print(flag)