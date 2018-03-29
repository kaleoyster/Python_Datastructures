## Python program to implement a queue
## Properties: 1. enqueue 2. dequeue 3. size 4. is_empty

class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

def main():
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    main()
