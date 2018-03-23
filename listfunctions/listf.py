from functools import reduce
## Demonstation of functools, itertools, lambda, map, filter

## Lambda expression
## filtering based on lambda expressions

## lambda expression  (lambda x: x%2 == 1)
l = [j for j in filter(lambda x: x%2  == 1, [i for i in range (1,20)])]
print(l)

## lambda expression filtering the odd squares which are divisible by 5
l = [j for j in filter(lambda x: x % 5 == 0,[ i**2  for i in range(11) if i % 2 == 1])]
print(l)

## lambda expression negative numbers
lst = [j for j in filter(lambda x: 0>x, [i for i in range(-5,6)])]
print(lst)

## implementing max() function reduce function
max_val = reduce(lambda a,b: a if a>b else b,[19,12,32,13,365,76,2])
print(max_val)

## implementing factorial 
fc = reduce(lambda x,y: x*y, range(1,6))
print(fc)
