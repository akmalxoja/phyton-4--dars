# Random sonlar orqali listni 20 ta element bilan to`ldiring, va listdagi juft sonlarni o`sish toq sonlarni kamayish tartibida chop eting.

import random
juft = list()
toq = list()

lst = [random.randint(1, 100) for i in range(20)]
print(lst)

for i in range(20):
    if i % 2 == 0:
        juft.append(i)
    else:
        toq.append(i)

print(sorted(juft))
toq.sort(reverse=True)
print(toq)