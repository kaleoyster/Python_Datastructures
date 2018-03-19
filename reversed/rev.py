
string = "apple"

text = ""
## Basic way of implementinf a reversed string in python
for i in reversed(string):
    text = text + i
## alternate method
#text = string[::-1]

print("The reversed  of "+string+" is: "+text)

