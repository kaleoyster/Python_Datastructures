## Python Program to reverse a string
## optimization consider using deque
## Create an empty stack
def createStack():
    stack = []
    return stack

## check if stack is empty
def isEmpty(stack):
    return len(stack) == 0

## push function
def push(stack,item):
    stack.append(item)

## pop function
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()

## reverse function
def reverse(string):
    n = len(string)

    stack = createStack()

    for i in range(0,n,1):
        push(stack,string[i])

    string=""

    for i in range(0,n,1):
        string = string + pop(stack)

    return string

print(reverse("Apple"))
