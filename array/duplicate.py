def removeDuplicates(myList):
    for i in range(len(myList)):
        if i==len(myList):
            return myList
        elif myList[i]==myList[i+1]:
            myList.remove(myList[i])


removeDuplicates([1, 1, 2, 2, 3, 4, 5])