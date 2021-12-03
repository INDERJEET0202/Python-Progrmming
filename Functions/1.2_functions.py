def my_function(fname, lname):
    print("Hi " + fname + " " + lname + " welcome")
my_function("Indrajit", "Pal")


#Arbitrary number of arguments
def welcome_function(*names):
    print("Hi " + names[0] + " " + names[1] + " welcome")
welcome_function("Indrajit", "Pal")

#Passing a dictionary
def dict(a1, a2, a3):
    print("Letter is " + a3)
dict(a1="Indrajit", a2="Pal", a3="A")


def arbitrary_dict(**letter):
    print("My first letter is " + letter["second"])
arbitrary_dict(first = "f" ,second = "s", third = "t")

#Default arguments
def default_arg(a3 = "A"):
    print("Letter is " + a3)
default_arg("N")
default_arg("B")
default_arg()

#List as an argument
def func(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
func(fruits)

#Returning a value
def add(a, b):
    return a + b
x = add(3, 5)
print(x)

#Pass statement
def add():
    pass
add()

# Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Function returning multiple values
def add_sub_multi_div(a, b):
    add = a + b
    sub = a - b
    multi = a * b
    div = a / b
    return add, sub, multi, div #returning multiple values
g = int(input("Enter a number: "))
h = int(input("Enter another number: "))
x, y, a, b = add_sub_multi_div(g, h)
print(x, y, a, b)
tuple = add_sub_multi_div(g, h)
# print("Results are ")
print("Results are " + str(tuple))

def ffunc(arg1, *argv):
    print(arg1)
    for arg in argv:
        print(arg)
ffunc('hi',1 ,2, 3, 4, 5)