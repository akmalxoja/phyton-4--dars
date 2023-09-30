from random import randint as rand

lst = list()

for i in range(20):
    lst.append(rand(1,41))

print(lst)

n = int(input('N = '))

for i in range(n):
    u = lst.pop()
    lst.insert(0,u)

print(lst)