def string_test(s):
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
string_test(Sample_String)