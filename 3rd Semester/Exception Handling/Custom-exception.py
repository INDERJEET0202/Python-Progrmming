class my_exception(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    if(a == b):
        raise my_exception("a and b cannot be same")
    result = a / b
    print("Result: ", result)
except(ValueError, ZeroDivisionError) as e:
    print("Error: ", e)
except my_exception as me:
    print("Error: ", me)
else:
    print("No Error")
finally:
    print("Bye")