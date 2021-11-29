# Write a python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic4 = {}
for d in (dic1, dic2): 
    dic4.update(d)
print(dic4)


key = (int(input("Enter the key: ")))
for x in dic1.keys():
    if(x == key):
        # print(dic1[key])
        print("Key already exists")
        break
else:
    print("Key not found")