file_name = "OOP/data.txt"
# f = open(file_name)
# f_contents = f.readline()
# f_contents = f.read()
# print(f_contents)
# f.close()

with open(file_name) as f:
    for line in f:
        print(line.strip())

record_to_add = "New record"
with open(file_name, "a+") as to_write:
    to_write.write(record_to_add + "\n")