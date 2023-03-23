# #Function to define all factors of a number
def all_the_factors_of_a_number(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter the number: "))
result = all_the_factors_of_a_number(number)
print(result)