import threading as thrd

def Ascd(From , To):
    with open("ascending.txt" , "w") as fl:
        for numb in range(From , To + 1):
            fl.write(str(numb))
            fl.write('\n')

def Prime(From , To):
    with open("prime.txt" , "w") as fl:
        for numb in range(From , To):
            IsDivAble = False
            for divider in range(2 , int(numb / 2) + 1):
                if numb % divider == 0:
                    IsDivAble = True
                    break
            if not IsDivAble:
                fl.write(str(numb))
                fl.write('\n')

if __name__ == "__main__":
    thrd1 = thrd.Thread(target = lambda: Ascd(1 , 1000000))
    thrd2 = thrd.Thread(target = lambda: Prime(1 , 200000))

    thrd1.start()
    thrd2.start()