# A Huffman Tree Node
import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def inorder_traversal(root, result):
    """Perform inorder traversal of the tree and collect node values."""
    if root:
        result.append(root.freq)
        inorder_traversal(root.left, result)

        inorder_traversal(root.right, result)


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
    # print(newVal,val,str(node.huff),'hai')
    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        # print('left',node.symbol)
        printNodes(node.left, newVal)
    if (node.right):
        # print('right',node.symbol)
        printNodes(node.right, newVal)

    # if node is edge node then
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}-{node.freq}")

    # characters for huffman tree


chars = ['e', 'a', 'd', 'b', 'c']

freq = [2, 3, 4, 5, 6]
original = ""
for i in range(len(chars)):
    original += (chars[i] * freq[i])
nodes = []
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    print(left.symbol, left.freq, right.symbol, right.freq)
    left.huff = 0
    right.huff = 1

    print(left.freq + right.freq, left.symbol + right.symbol, left.symbol, right.symbol)
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    heapq.heappush(nodes, newNode)

printNodes(nodes[0])
result = []
inorder_traversal(nodes[0], result)
print(result)
print(original)

















