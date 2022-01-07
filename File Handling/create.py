from typing import final


try:
    f = open("File Handling/python.txt", "w")
    f.write("Hello World.")
    f = open("File Handling/python.txt", "r")
    # print(f.read(4)) # Read(size)
    print(f.readline()) # Readline()
    print(f.tell()) # Tell()
finally:
    f.close()