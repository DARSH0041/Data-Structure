class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
        self.lst = []
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if data <= temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    else:                        temp = temp.left
                elif data > temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right
    def print_inorder1(self, node,data):
        if node:
            self.print_inorder1(node.left,data)
            if data<node.data:
                self.lst.append(node.data)
            self.print_inorder1(node.right,data)
    def print_inorder2(self, node):
        if node:
            self.print_inorder2(node.left)
            self.print_inorder1(self.root,node.data)
            print(self.lst)
            node.data+=sum(self.lst)
            self.print_inorder2(node.right)
            self.lst = []
    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(node.data, end=">")
            self.print_inorder(node.right)
obj = Tree()
elements = [50,20,30,10,40,60,70]
for elem in elements:
    obj.insert(elem)
obj.print_inorder2(obj.root)
obj.print_inorder(obj.root)
print(obj.lst)