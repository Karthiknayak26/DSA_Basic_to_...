class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class binarytree:
    def __init__(self):
        self.root=None

    def  inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def preorder(self,root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

bt=binarytree()
bt.root=node(10)
bt.root.left=node(20)
bt.root.right=node(30)
bt.root.left.left = node(40)
bt.root.left.right = node(50)
bt.inorder(bt.root)
bt.postorder(bt.root)
bt.preorder(bt.root)

