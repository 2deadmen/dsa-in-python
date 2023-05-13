class MinStack(object):

    def __init__(self):
        self.topi=-1
        self.stack=[]
        self.min=[0]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.topi+=1
        if val <= self.min[-1]:
            self.min.append(val)
        

        

    def pop(self):
        """
        :rtype: None
        """
        self.topi-=1
        ele=self.stack.pop()
        if ele==self.min[-1]:
            self.min.pop()
        return ele

    def top(self):
        """
        :rtype: int
        """
        ele=self.stack[self.topi]
        return ele

    def getMin(self):
        """
        :rtype: int
        """
        print(self.min)
        ele=self.min[-1]
        return ele
    
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
obj.pop()
print(obj.getMin())
print(obj.pop())
# print(obj.top())
print(obj.getMin())
