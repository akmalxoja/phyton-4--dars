n = int(input("n = "))
lst = [1, 2, 33, 5, 6, 7, 7]

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] + lst[j] == n and i < j:
            print(f"{i} : {j}")
