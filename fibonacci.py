# 0 1 1 2 3 5 
res = [0]

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res.append(fibo(n-1) + fibo(n-2))
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter a number: "))
print(fibo(n))
print(set(res))