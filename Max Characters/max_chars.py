## Python program to return a character with a maximum number of count in a string.
## for eg: max_chars("Apple") = "p"  Because, p = 2, and a = 1, l = 1 and e = 1
##         max_char("Killmonger") = "l" Because, l = 2, and k = 1, i = 1, m = 1,o = 1, n = 1, g = 1, e = 1, r = 1

## utility function to count maximum number of character
def maxch(dic):
    mx = 0 
    ch = ""
    for key, val in dic.items(): 
        if mx < val:
            mx = val 
            ch = key
    return ch

def max_char(string):
    ## convert into lower string
    string = string.lower()
   
   ## initialize a dictionary  
    d = { ch:0 for ch in string}
   
   ## keep a count of all letters
    for ch in string:
        d[ch]+=1
    return maxch(d)

## driver function
if __name__ == "__main__":
    string = input("Enter string: ")
    print(max_char(string))
