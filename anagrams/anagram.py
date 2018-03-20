import re

## Check for anagrams 
## Solving Anagrams using sort method
def anagram(string1,  string2):
    return cleaned(string1) == cleaned(string2)

## Need to write a clean replace function.
## Need to write alternate methods using dictionary.
def cleaned(string):
    ## replace special character with 
    ## str.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")
    ## to lower case string = string.lower()
    ## to splitstring = str
    ## to sort string = sorted(string)
    ## to join string = "".join(string)
    escapes = "!@#$%^&*()[]{};:,./<>?\|`~-=_+"
    esc = [e for e in escapes]
    for es in esc:
        string = string.replace(es,"")
    string = string.lower()
    #string = string.split('')
    string = sorted(string)
    string = "".join(string)

    return string

if __name__=="__main__":
   #string = "rail! safety!"
   #string1 = "fairy tales"
   string = input("Enter first string: ")
   string1 = input("Enter second string: ")
   print(anagram(string,string1))

