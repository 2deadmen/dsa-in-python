import random

list=[1,2,3,4,5]
list1=[]
list2=[]
list3=[]
lists=[list1,list2,list3]
prev=[1] 
for i in list:
    l=random.choice(lists)
    prev.append(l)
    while True:
         if prev[i-1]==l or len(l)>=2:
            l=random.choice(lists)
         else:
            break
    l.append(i)

print(list1)
print(list2)
print(list3)
    