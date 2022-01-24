# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funArgs(normal, *args, **kwargs): #normal args will always be the first one in the function and then the *args and then the **kwargs
    print(normal)
    for i in args:
        print(i,end = ", ")
    print()
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

normal = "I am a normal argument"
kwargs = {"Rohan": "Moniter", "Raj": "Developer", "Rajesh": "Tester", "Shivam": "Manager"}

l = ["Raj", "Indra", "Jit", "Indrajit"]
funArgs(normal, *l, **kwargs)