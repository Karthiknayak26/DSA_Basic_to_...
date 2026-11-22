class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bst:
    def __init__(self):
        self.root=None

    def insert(self,root,data):
        if root is None:
            return node(data)
        elif data<root.data:
            root.left=self.insert(root.left,data)

        elif data>root.data:
            root.right=self.insert(root.right,data)

        return root
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def search(self,root,data):
        if root is None:
            return False
        elif root.data==data:
            return True
        elif data<root.data:
            return self.search(root.left,data)
        elif data>root.data:
            return self.search(root.right,data)
    def find_min(self,root):
        if root is None:
            return None
        current=root
        while current.left is not None:
            current=current.left
        return current.data

    def find_max(self,root):
        if root is None:
            return None
        current=root
        while current.right is not None:
            current=current.right
        return current.data
    def delete(self,root,data):
        if root is None:
            return None
        elif data<root.data:
            root.left=self.delete(root.left,data)
        elif data>root.data:
            root.right=self.delete(root.right,data)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor=self.find_min(root.right)
                root.data=successor
                root.right=self.delete(root.right,successor)
        return root
    

    

bst=bst()
value=[40,50,60,20]
for val in value:
    bst.root=bst.insert(bst.root,val)

bst.inorder(bst.root)
print(bst.search(bst.root,20))

print(bst.find_max(bst.root))
bst.root=bst.delete(bst.root,50)
bst.inorder(bst.root)

