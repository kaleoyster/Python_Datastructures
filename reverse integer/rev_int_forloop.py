## Python Program to reverse an integer'

def rev_int(string):
    l = list(str(int(string)))
    n = 0

    if l[0] == '-':
       n = 1
       l = l[1:]
    l = reverse_l(l)
    ri = "".join(l)
    if n == 1:
       ri = 0 - int(ri)
    return int(ri)


def reverse_l(l):
    rev_l = [i for i in reversed(l)]
    return rev_l

if __name__ == "__main__":
    integer = input("enter an integer: ")
    print(rev_int(integer))
