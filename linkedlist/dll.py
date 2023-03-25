class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None

        
    def create(self):
        newNode=Node(0)
        self.head=newNode
        newNode.next=None
        newNode.prev=None
        self.tail=newNode

    def insert(self,value,loc):
        newNode=Node(value)
        if loc==0:
            self.head.prev=newNode
            newNode.next=self.head
            newNode.prev=None
            self.head=newNode
        elif loc==-1:
            newNode.prev=self.tail
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode
        else:
            tempNode=self.head
            index=0
            while index < loc -1:
                tempNode=tempNode.next
                index+=1
            nextNode=tempNode.next
            nextNode.prev=newNode
            tempNode.next=newNode
            newNode.prev=tempNode
            newNode.next=nextNode

    def traverse(self):
          if self.head is self.tail:
            print(" The dll's existence ceases to exist....hahahaha")
          else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    def traverse_reverse(self):
          if self.head is self.tail:
            print(" The dll's existence ceases to exist....hahahaha")
          else:
            node=self.tail
            while node is not None:
                print(node.value)
                node=node.prev
        
    def delete(self,loc):
        if self.head is self.tail:
            print(" The dll's existence ceases to exist....hahahaha")

        else:
            if loc == 0:
                node=self.head
                self.head=self.head.next
                node.next=None
                self.head.prev=None
            elif loc==99:
                self.head=None
                self.tail=None
            elif loc == -1:
                node=self.tail.prev
                self.tail.prev=None
                self.tail=node
                self.tail.next=None
            else:
                tempNode=self.head
                index=0
                while index < loc-1:
                    tempNode=tempNode.next
                    index+=1
                node=tempNode.next
                nextNode=node.next
                nextNode.prev=tempNode
                tempNode.next=nextNode

ddl=DLL()
ddl.create()
ddl.insert(1,0)
ddl.insert(2,-1)
ddl.insert(1,1)
ddl.traverse()
print("\n")
ddl.delete(-1)
ddl.traverse()
print("\n")
ddl.traverse_reverse()