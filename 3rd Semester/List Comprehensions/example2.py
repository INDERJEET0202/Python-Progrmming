# Dictionary comprehension

dict1 = {0: "item0"}
print(dict1)

dict0 = {
    i: f"Item{i}" for i in range(1, 1001) if i % 100 == 0
}

dict1 = {
    i: f"Item{i}" for i in range(5)
}
print(dict1)
dict1 = {value:key for key, value in dict1.items()}
print(dict1)