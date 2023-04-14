class Tree:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None

    
def insert(root,value):
        list=[]
        list.append(root)
        while list!=[]:
            root=list[0]
            list=list[1:]
            if root.left==None:
                root.left=Tree(value)
                break
            if root.right==None:
                root.right=Tree(value)
                break
            list.append(root.left)
            list.append(root.right)

def delete(root,value):
        list=[]
        list.append(root)
        while list!=[]:
            root=list[0]
            list=list[1:]
            if root.left.value==value:
                root.left=None
                break
            if root.right.value==value:
                root.right=None
                break
            if root.left != None:
                list.append(root.left)
            if root.right != None:
                list.append(root.right) 


tree=Tree(1)
left=Tree(2)
right=Tree(3)
tree.left=left
tree.right=right
subleft=Tree(4)
left.left=subleft
subright=Tree(5)
left.right=subright




def preorderTraverse(root):
    if not root:
        return
    print(root.value)
    preorderTraverse(root.left)
    preorderTraverse(root.right)


def inorderTraverse(root):
    if not root:
        return

    inorderTraverse(root.left)
    print(root.value)
    inorderTraverse(root.right)


def postorderTraverse(root):
    if not root:
        return
    postorderTraverse(root.left)
    postorderTraverse(root.right)
    print(root.value)

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
       



lvlorder(tree)
insert(tree,6)
print("\n")
lvlorder(tree)
delete(tree,6)
print("\n")

lvlorder(tree)
# preorderTraverse(tree)
# print("\n")
# postorderTraverse(tree)
# print("\n")
# inorderTraverse(tree)
