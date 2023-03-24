class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SSl:
    def __init__(self,value=None):
        self.head=None  
        self.tail=None

    def insert(self,value,loc):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            #inserting an element at the start
            if loc == 0:
        
                newNode.next=self.head
                self.head=newNode
            #inserting an element at the end
            elif loc== -1:
                node=self.head
                while node is not self.tail:
                    node=node.next
                node.next=newNode
                newNode.next=None
                self.tail=newNode
            #inserting an element at the given position
            else:
                tempNode=self.head
                index=0
                while index < loc -1:
                    tempNode=tempNode.next
                    index +=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode   
    #traversing and printing
    def traverse(self):
        if self.head is None:
            print("the ssl is empty")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    #deleting a node
    def delete(self,loc=99):

        if self.head is None:
            print("the ssl is empty")
        else:

            if loc==0:
                self.head=self.head.next
            elif loc==99:
                self.head=None
                self.tail=None
                print("the whole ssl is deleted")
            elif loc== -1:
                node=self.head
                while node.next is not self.tail:
                    node=node.next
                node.next=None
                self.tail=node
            else:
                tempNode=self.head
                index=0
                while index < loc-1:
                    tempNode=tempNode.next
                    index+=1
                node=tempNode.next
                tempNode.next=node.next


ssl=SSl()
ssl.insert(1,0)
ssl.insert(2,0)
ssl.insert(3,-1)
ssl.insert(2,1)
ssl.traverse()
print("\n")
ssl.delete(2)
ssl.traverse()
ssl.delete(99)
ssl.traverse()