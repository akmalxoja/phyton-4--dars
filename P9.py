num = input("Son: ")

num = num.split()
num = list(map(int,num))

text_num = str()

for i in num:
    text_num+=str(i)
    
text_num = int(text_num)
text_num+=1
text_num = str(text_num)
num.clear()

num.extend(map(int,text_num))

print(num)