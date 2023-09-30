nums = list(map(int,input("Sonlarni kitinting: ").split()))

a = (sorted(nums))
a.reverse()

if nums == a:
    print("Kamayish tartibida")

elif nums == sorted(nums):
    print("O'sish tarribida")

else:
    print("Tartibsiz")