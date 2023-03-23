# lambda arguments: expression (syntax)

x = lambda a: a + 50 #passing one arguments
print(x(5))

y = lambda a, b: a * b #passing two arguments
print(y(5, 6))

z = lambda a, b, c: a + b + c #passing three arguments
print(z(5, 6, 10))




def func(n):
    return lambda a: a * n
d = func(2)
print(d(11))

f = lambda x: x + x
var = f(5)
print(var)