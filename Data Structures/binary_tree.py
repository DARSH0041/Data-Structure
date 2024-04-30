class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp1 = temp = self.root
            flag = 0
            while True:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                elif temp.right is None:
                    temp.right = Node(data)
                    break
                elif flag == 0:
                    temp = temp1.left
                    flag = 1
                elif flag == 1:
                    temp = temp1.right
                    flag = 0
    def display(self):
        print("inorder")
        self.inorder(self.root)
        """print("\npreorder")
        self.preorder(self.root)
        print("\npostorder")
        self.postorder(self.root)"""


    def inorder(self, root):
        if (root):
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    """def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")"""


bt = BT()
lst = [1, 2, 3, 4, 5, 6, 7]
for i in lst:
    bt.insert(i)
bt.display()