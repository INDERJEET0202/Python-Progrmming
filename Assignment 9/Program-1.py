def addis(str):
    # if(str[:2] == "is"): # Method 1
    if(str.startswith('is') or str.startswith('Is')): # Method 2
        return str
    else:
        return "is " + str
string = str(input("Enter your string - "))
string = addis(string)
print(string)