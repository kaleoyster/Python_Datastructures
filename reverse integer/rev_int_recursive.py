## Python Program to reverse an integer
## using recursion


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

def reverse(int_list):
    if len(int_list) == 0:
       return int_list
    else:
        return reverse(int_list[1:]) + int_list[0]
if __name__ == "__main__":
    integer = input("enter an integer: ")
    print(rev_int(integer))
