lst = ['abc', 'xyz', 'bo\'lib','aba', '1221']
count = 0
for i in range(len(lst)):
    if lst[i][0] == lst[i][-1] and len(lst[i]) > 2:
        count += 1

print(count)      