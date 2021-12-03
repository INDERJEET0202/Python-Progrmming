#Method 1
def string(s):
    dict = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
           dict["UPPER_CASE"] = dict["UPPER_CASE"] + 1
        elif c.islower():
           dict["LOWER_CASE"] = dict["LOWER_CASE"] + 1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", dict["UPPER_CASE"])
    print ("No. of Lower case Characters : ", dict["LOWER_CASE"])
Sample_String = "The quick Brown Fox"
string(Sample_String)


#Method 2
def string(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
           upper = upper + 1
        elif c.islower():
            lower = lower + 1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", upper)
    print ("No. of Lower case Characters : ", lower)
Sample_String = "The quick Brown Fox"
string(Sample_String)