def gcd(n1, n2):
    # if n2 == 0:
    #     return n1
    # else:
    #     return gcd(n2, n1 % n2)
    
    # while n2 != 0:
    #     n1, n2 = n2, n1 % n2
    # return n1

    #using turnery operator
    return n1 if n2 == 0 else gcd(n2, n1 % n2)


n1, n2 = map(int, input().split())
print(gcd(n1, n2))