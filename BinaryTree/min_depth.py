class Node:
    def __init__(self,key):
       self.data=key
       self.left = None
       self.right = None


def MinDepth(node):

    if node is None:
         return 0

    if node.left is None and node.right is None:
         return 1
     
    if node.left is None:
         return MinDepth(node.right)+1
     
    return max(MinDepth(node.left), MinDepth(node.right))+ 1



root = Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(MinDepth(root))
