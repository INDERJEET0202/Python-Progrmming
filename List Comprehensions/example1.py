# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
# print(ls)

ls = [i for i in range(100) if i % 3 == 0 and i % 5 == 0]

print(ls)