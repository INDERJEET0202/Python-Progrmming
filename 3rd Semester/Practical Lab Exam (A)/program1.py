def func(list1, length, l5):
    res = False
    def count(list, l5):
        count = 0
        for i in range(len(list)):
            if list[i] == l5:
                count += 1
        return count
    # if(len(list1) == 8 and list1.count(list1[4]) == 3):
    if(len(list1) == 8 and count(list1, l5) == 3):
        res = True
    return res

l = list(map (int, input().split()))
length = len(l)
l5 = l[4]

print(func(l, length, l5))
