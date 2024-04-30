class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    else:
                        temp = temp.left
                elif data > temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right
    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(node.data, end=" ")
            self.print_inorder(node.right)

    def print_preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node):
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.data, end=" ")

    def find_recursive(self, data, node):  # Data not found
        if node is None:
            return None
        if data == node.data:
            print('True')
        elif data > node.data:
            return self._find_recursive(data,node.right)
        elif data < node.data:
            return self._find_recursive( data,node.left)
        else:
            print("data no in tree")
    def search(self,node,data):
        if node is not None:
            if node.data==data:
                print("True")
            elif node.data<data:
                self.search(node.right,data)
            elif node.data>data:
                self.search(node.right,data)
        else:
            print("False")

    def removeLeaves(self,root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return None  # Remove leaf node
        root.left = self.removeLeaves(root.left)
        root.right = self.removeLeaves(root.right)
        return root

    def minValueNode(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self,root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        elif key > root.data:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.deleteNode(root.right, temp.data)

        return root
obj = Tree()
elements = [20,10,5,15,30,25,35]
for elem in elements:
    obj.insert(elem)
#obj.search(obj.root,9)
print("In-order traversal:")
obj.print_inorder(obj.root)
print("\n")
"""obj.removeLeaves(obj.root)
print("In-order traversal:")
obj.print_inorder(obj.root)
print("\n")"""
"""print("Pre-order traversal:")
obj.print_preorder(obj.root)
print("\n")
print("Post-order traversal:")
obj.print_postorder(obj.root)
print("\n")"""
"""obj.find_recursive(20,obj.root)
obj.search(obj.root,20)"""
obj.deleteNode(obj.root,5)
obj.print_inorder(obj.root)
print()
obj.deleteNode(obj.root,15)
obj.print_inorder(obj.root)