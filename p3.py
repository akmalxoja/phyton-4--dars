lst = [23, 44, 56, 99, 111, 23, 54]

for i in range(len(lst)):
    if(lst[i] % 2 == 0):
        del(lst[i])

print(lst)