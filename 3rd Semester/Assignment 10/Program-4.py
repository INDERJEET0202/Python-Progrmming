# Write a Python Function that checks weather a passed string is Palindrome or not.

def palindrome(str):
    str = str.replace(" ", "")
    str = str.lower()
    if str == str[::-1]:
        return True
    else:
        return False

str = input("Enter a string: ")
if palindrome(str):
    print(str)
else:
    print("False")