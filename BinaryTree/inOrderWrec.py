# class node:
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None
#
# def inorder(root):
#     #(left, root, right)
#     current = root
#     # initialize stack
#     stack = []
#
#     done = 0
#
#     while (not done):
#         if current is not None:
#             stack.append(current)
#             current = current.left
#
#         else:
#             if(len(stack)>0):
#                 current = stack.pop()
#                 print(current.data)
#                 current = current.right
#
#             else:
#                 done = 1
#

class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def inorder(root):
    # (left, root, right)
    current  = root
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
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

    inorder(root)
