## Python program to reverse words in a string
## Eg.  'Hello World' - > 'olleH dlroW'

def rev_str(string):
    rev1 = [i for i in reversed("".join([ch for ch in reversed(string)]).split(" "))]
    return " ".join(rev1)

if __name__ == "__main__":
    string = input("Enter string : " )
    print(rev_str(string))
