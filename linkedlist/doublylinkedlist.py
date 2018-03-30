## Python Implementation of a doubly-linked list.

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def traverse_front(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
'''
def main():
    n = input("Enter the Length of Linked list: ")
    print("Enter the numbers")
    # Node is head
    for index in range(0,len(n),1):
        number = input()
        node = DoublyNode(number)
    node1 = DoublyNode(1)
    node2 = DoublyNode(2)
    node3 = DoublyNode(3)
    
    node1.next = node2
    node2.next = node3

    node1.traverse_front()
'''

def main():

    node1 = DoublyNode(1)
    node2 = DoublyNode(2)
    node3 = DoublyNode(3)

    node1.next = node2
    node2.next = node3

    node1.traverse_front()
if __name__ == "__main__":
    main()

