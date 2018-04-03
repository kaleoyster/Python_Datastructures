## Python Program to count vowels in a string
def countVowels(string):
    string = string.lower()
    Vcount = 0
    vowels = {'a','e','i','o','u'}
    for i in string:
        if i in vowels:
            Vcount = Vcount + 1
    return Vcount

# Driver Function
if __name__=='__main__':
    string = input("Enter String: ")
    print(countVowels(string))
