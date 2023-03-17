from array import *
arr=array('i',[1,8,3,5,6])
biggest=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        num=arr[i]* arr[j]
        if num > biggest:
            biggest=num
print(biggest)
