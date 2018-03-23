## Program to capitalize first letter of the word

def capitalize(string):
    k = [i[0].upper()+i[1:] for i in string.split(" ")]
    return (" ".join(k))

if __name__ == "__main__":
    string = input("Enter string: ")
    print(capitalize(string))
