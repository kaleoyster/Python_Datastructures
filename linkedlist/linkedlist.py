# A Python implementation of Linked List
# Author: Akshay Kale

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self ## start from the head of the node
        while node != None:
            print(node.val) ## print the value of the node
            node = node.next ## move on to the next node

def main():
    node1 = Node(12)
    node2 = Node(13)
    node3 = Node(14)

    node1.next = node2
    node2.next = node3
    
    node1.traverse()

if __name__ == "__main__":
    main()
