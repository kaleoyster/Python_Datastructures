## Python Program to reverse a string
## using recursion

#string = "Apple"
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0] ## reverse(s[1:]) decreses the len by 1
string = input("Enter string: ")
print(reverse(string))
print(type(reverse(string)))
