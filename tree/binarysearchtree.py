class Tree:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None

    
def insert(root,value):
        while root != None:
            if value < root.value:
                if root.left==None:
                    root.left=Tree(value)
                    break
                else:
                    root=root.left
            
            if value > root.value:
                if root.right==None:
                    root.right=Tree(value)
                    break
                else:
                    root=root.right
  


def delete(root,value):
        while root!= None:
            if root.value > value:
                
                if root.left.value == value:
                    root.left=None
                    break
                if root.left != None:
                    root=root.left

            if root.value < value:
                
                if root.right.value == value:
                    root.right=None
                    break
                if root.right != None:
                    root=root.right

def lvlorder(root):
    if not root:
        return
    list=[]
    list.append(root)
    while list!=[]:
        root=list[0]
        print(root.value)
        list=list[1:]
        if root.left != None:
            list.append(root.left)
        if root.right != None:
            list.append(root.right)
tree=Tree(10)
lvlorder(tree)
print("\n")
insert(tree,9)
insert(tree,11)
insert(tree,8)
lvlorder(tree)
delete(tree,9)

print("\n")
lvlorder(tree)

