
def ffunc(arg1, *argv):
    print(arg1)
    for arg in argv:
        print(arg)
ffunc('hi',1 ,2, 3, 4, 5)