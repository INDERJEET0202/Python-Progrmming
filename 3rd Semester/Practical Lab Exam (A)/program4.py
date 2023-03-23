s = input()
l = list(map(str, s.split("-")))
# print(l)
l = sorted(l)
# for i in range(len(l)):
s = "-".join(l)
print(s)