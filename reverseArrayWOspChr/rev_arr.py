


def isAlphabet(string):
    return string.isalpha()

def reverse(string):
    LIST  = toList(string)
    r = len(LIST) - 1
    l = 0


    while l < r:
        if not isAlphabet(LIST[l]):
            l += 1
        elif not isAlphabet(LIST[r]):
            r -= 1
        else: 
            LIST[l], LIST[r] = LIST[l], LIST[r]
            l += 1
            r -= 1

    return toString(LIST)

def toList(string):
    return [i for i in string]

def toString(List):
    return ''.join(List)


string = 'a!!!b.c.d,ef,ghi'
print(reverse(string))

