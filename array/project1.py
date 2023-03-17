from array import *
arr=array('i')
n=int(input("enter the number of days"))
for i in range(n):
    var=int(input("enter temp"))
    arr.append(var)

avg=sum(arr)/len(arr)
count=0
for i in arr:
    if i > avg:
        count+=1
print("the average temperature is",avg)
print(count , "day(s) temp are higher then the average temperature")
