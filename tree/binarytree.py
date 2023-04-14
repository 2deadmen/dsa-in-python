class Tree:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
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


preorderTraverse(tree)
print("\n")
postorderTraverse(tree)
print("\n")
inorderTraverse(tree)
