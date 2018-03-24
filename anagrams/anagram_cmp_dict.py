

def buildCharMap(string):
    charMap = {i:0 for i in string}
    for i in string:
        charMap[i] = charMap[i] + 1
    return charMap

def cleaned(string):
    escapes = "!@#$%^&*(){}|:<>`~,./? "
    escapes = [e for e in escapes]
    for es in escapes:
        string = string.replace(es,"")
    string = string.lower()
    return string

def checkAnagram(string1, string2):
    charMapString1 = buildCharMap(string1)
    charMapString2 = buildCharMap(string2)
    return charMapString1 == charMapString2


if __name__ == "__main__":
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    print(checkAnagram(string1,string2))

