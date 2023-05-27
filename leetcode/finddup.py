slow=0
nums=[1,3,4,2,2]
fast=0
while True:
    if nums[slow]==nums[fast]:
        print (nums[fast])
        break
    else:
        fast +=2
        slow +=1