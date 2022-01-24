tupe = tuple(input().split())
l = []
for i in range(len(tupe)):
    for j in range(i+1, len(tupe)):
        if tupe[i] == tupe[j]:
            l.append(tupe[i])

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            l.remove(l[i])
print(l)
