from collections import deque

string = 'apple'
reversed_string = deque()

for s in string:
    reversed_string.appendleft(s)

reversed_string  = "".join(reversed_string)
print(reversed_string)

