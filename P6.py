nums1 = [1, 2]
nums2 = [11, 22, 33, 44, 55]
nums3 = list()

if len(nums1) <= len(nums2):
    for i in range(len(nums2)):
        if i < len(nums1):
            nums3.append(nums1[i])
        nums3.append(nums2[i])
else:
    for i in range(len(nums1)):
        nums3.append(nums1[i])
        if i < len(nums2):
            nums3.append(nums2[i])

print(nums3)