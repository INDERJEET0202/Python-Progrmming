def my_math_function(x, f):
    return f(x)

def x_cube(x):
    return x**3

my_lambda = lambda x: x**3

print(my_math_function(5, x_cube))
print(my_math_function(5, lambda x: x**3)) #Using lambda, same as above
print(my_lambda(5))
print(my_lambda(3))
print(my_lambda(4))

# Quick look how math function works
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(list(map(str.capitalize, my_letters)))
print(list(map(lambda x: x + x.capitalize(), my_letters)))

# Printing random integers
from random import randint
my_ints = [randint(1, 1000) for i in range(100)]
print(my_ints)
print(list(map(lambda x: x**3, my_ints)))