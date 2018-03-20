## Python Program to reverse an integer


def rev_int(string):
    l = list(string)
    n = 0
    if l[0] == '-':
       n = 1
       l = l[1:]
    l = l[::-1]
    ri = "".join(l)
    if n == 1:
       ri = 0 - int(ri)
    return int(ri)

if __name__ == "__main__":
    integer = input("enter an integer: ")
    print(rev_int(integer))
