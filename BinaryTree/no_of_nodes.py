class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None


def countNode(node):
    if node is None:
       return 0
    if node.left is None and node.right is None:
       return 0
    else:
       return countNode(node.left) + 1 + countNode(node.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left = Node(5)
root.left.right = Node(6)

print(countNode(root))
