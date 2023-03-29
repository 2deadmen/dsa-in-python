from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        newNode=Node(values)
        self.head = newNode
        self.tail = newNode

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode=Node(value)
            self.tail.next = newNode
            newNode.prev=self.tail
            newNode.next=None
            self.tail = newNode
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
    
    def removedups(self):
        authentic=[]
        node=self.head
        while node is not None:
            if node.value in authentic:
                temp=self.head
                while temp.next != node:
                    temp=temp.next
                temp.next=node.next
                
            else:
                authentic.append(node.value)
                
            node=node.next

    def returnnthfromlast(self,n):
        length=self.__len__()            
        pos=length-n
        node=self.head
        index=0
        while index is not pos:
            node=node.next
            index+=1
        return node 
    
    def sum_ll(self):
        ll1=LinkedList(0)
        ll2=LinkedList(0)
        ll1.addstart(1)
        ll1.addstart(0)
        ll1.addstart(1)
        ll2.addstart(1)
        ll2.addstart(0)
        ll2.addstart(1)
        print(ll1)
        print(ll2)
        temp=ll1.tail
        llstr=""
        while temp is not None:
            llstr+=str(temp.value)
            temp=temp.prev
            
        llstr1=""
        temp1=ll2.tail
        while temp1 is not None:
            llstr1+=str(temp1.value)
            temp1 = temp1.prev
        llstr=int(llstr)
        llstr1=int(llstr1)
        final=llstr+llstr1
        finalll=LinkedList(0)
        while final > 0:
            num=final%10
            finalll.addstart(num)
            final=round(final/10)
        print(finalll)

    def addstart(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head.prev=newNode
        self.head=newNode
        newNode.prev=None

    def createintersect_andfindintersectnode(self):
       #creating intersected linked lists
        ll1=LinkedList(0)
        ll2=LinkedList(0)
        ll1.add(1)
        ll1.add(2)
        ll1.add(3)
        ll1.add(4)
        ll1.add(9)
        ll2.add(3)
        ll2.add(5)
        node=ll1.head
        index=0
        print(ll1)
        print(ll2)
        while index < 3:
            node=node.next
            index+=1
        
        ll2.tail.next=node
        ll2.tail=ll1.tail
        print(ll1)
        print(ll2)

        #finding and returning the intersecting node
        n1=ll1.head
        n2=ll2.head
        while n1.next != n2.next :
            n1=n1.next
            n2=n2.next
        print(n1.next)


        
    def partition(self,n):
        customLL1=LinkedList()
        temp=self.head
        while temp is not None:
            if temp.value >= n:
                customLL1.add(temp.value)
                temp=temp.next
            else:
                customLL1.addstart(temp.value)
                temp=temp.next
        print(customLL1)

customLL = LinkedList()
#customLL1 = LinkedList()

#customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))
#remove diplicates


# customLL.add(10)
# customLL.add(1)
# customLL.add(6)
# customLL.add(2)
# customLL1.add(0)
# customLL1.add(0)
# customLL1.add(1)
# customLL.add(7)
# print(customLL)
# print(customLL1)
# customLL.removedups()
# print(customLL)
#customLL.partition(5)
#print(customLL.returnnthfromlast(2))


#sum of two linked list
#customLL.sum_ll()
#creating intersecting linked lists
customLL.createintersect_andfindintersectnode()
