try:
    f = open("ascending.txt", "w")
    for i in range (1, 1000000+1):
        # print(i)
        f.write(str(i) + "\n")

    for number in range (1, 200000 + 1):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:  
                i = open("prime.txt", "w")
                # print (number)
                i.write(str(number) + "\n")

finally:
    f.close()
    i.close()