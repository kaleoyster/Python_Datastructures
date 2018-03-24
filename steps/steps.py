## A function that accepts the positive number N.
## The function should console log a step change.
## with N levels uing #  characters

def steps(n):
    for i in range(int(n)+1):
        print('#'*i)

if __name__=='__main__':
    n = input("Enter levels: ")
    steps(n)
