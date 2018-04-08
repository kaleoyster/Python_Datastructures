class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def inorder(root):
        #(left, root, right)
        current = root
        # initialize stack
        stack = []

        done = 0

        while (not done):
            if current is not None:
                stack.append(current)
                current = current.left

            else:
                if(len(stack)>0):
                    current = stack.pop()
                    print(current.data)
                    current = current.right

                else:
                    done = 1

if __name__== "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    inorder(root)
