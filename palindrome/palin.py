## Python Program check for a palindrome 

def checkPalin(string):
     return string  == string[::-1]

if __name__ == "__main__":
    string = "abbba"
    print(checkPalin(string))
