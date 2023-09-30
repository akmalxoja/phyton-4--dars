n = input("Enter latter: ")
n = n.split()
print(n)
new = list()

row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

for i in n:

    c1 = 0
    c2 = 0
    c3 = 0 
    for j in i:
        if j in row1:
            c1+=1
        elif j in row2:
            c2+=1    
        elif j in row3:
            c3+=1

    if c1 == len(i):
        new.append(i)

    elif c2 == len(i):
        new.append(i)

    elif c3 == len(i):
        new.append(i) 

print(new)                             