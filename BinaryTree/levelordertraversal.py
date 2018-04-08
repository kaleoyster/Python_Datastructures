class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None



def printlevelorder(node):
    if node is None:
        return
    else:
        queue = []
        queue.append(node)
        length_que = len(queue)
        while length_que >= 1:

            print(queue[0].data)
            node = queue.pop(0)

            if node.left is not None:
                 queue.append(node.left)

            if node.right is not None:
                 queue.append(node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print("Level order traversal of binary tree ")
printlevelorder(root)
