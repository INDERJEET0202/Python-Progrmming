# Generators, yield

li = [num for num in range(1, 11)]

my_cubed_inits = map(lambda x: x**3, li)
# print(list(my_cubed_inits))
# print(next(my_cubed_inits))

def mash_map(f, some_iterable):
    result = []
    for item in some_iterable:
        result.append(f(item))
        yield f(item)
    return result

def mash_map(f, some_iterable):
    for item in some_iterable:
        yield f(item)


def mash_map(f, some_iterable):
    return [f(item) for item in some_iterable]

print(li)
my_cubed_inits = mash_map(lambda x: x**3, li)
print(my_cubed_inits)
# print(next(my_cubed_inits))
# print(next(my_cubed_inits))
# print(next(my_cubed_inits))
# print(list(my_cubed_inits))
