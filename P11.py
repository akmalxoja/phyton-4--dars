num = int(input("Ikkilik sanoq sistemasiga o'tkazilgan sonni kiriting: "))

count = 0
while num % 2 == 0:
    count += 1
    num = num // 2

print("Nollar soni:", count)