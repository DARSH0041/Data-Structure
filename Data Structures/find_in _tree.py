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
                if data <= temp.data:
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

    def _find_recursive(self, node, data):
        if node is None:
            return None  # Data not found
        if data == node.data:
            return node.data
        elif data > node.data:
            return self._find_recursive(node.right, data)
        elif data < node.data:
            return self._find_recursive(node.left, data)

    def find(self, data):
        return self._find_recursive(self.root, data)

# Example usage
obj = Tree()
elements = [1, 5, 6, 7, 8, 2, 3, 4]
for elem in elements:
    obj.insert(elem)

print("In-order traversal:")
obj.print_inorder(obj.root)
print("\n")

search_values = [10, 6, 2]
for value in search_values:
    result = obj.find(value)
    if result:
        print(f"Found {value} in the tree.")
    else:
        print(f"{value} not found in the tree.")
