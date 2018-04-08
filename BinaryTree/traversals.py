class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printInorder(root):
    #(left, root, right)
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

def printPostorder(root):
    #(left,right,root)
    if root:

        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

def printPreorder(root):
    #(root,left,right)
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(printInorder(root))
