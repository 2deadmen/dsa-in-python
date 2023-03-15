
  new=[]
def capitalizeFirst(arr):
  
    if len(arr)==0:
        return new
    else:
        string=arr[0].title()
        new.append(string)
        return capitalizeFirst(arr[1:])
print(capitalizeFirst(['car', 'taco', 'banana']))
# arr=['car', 'taco', 'banana']
# new=[]
# for i in arr:
#     str=i.title()
#     new.append(str)
# print(new)
