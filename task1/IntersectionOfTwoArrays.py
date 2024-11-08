def intersection(nums1, nums2):
    arr1 = set(nums1)
    arr2 = set(nums2)

    return list(set.intersection(arr1, arr2))


nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

print(intersection(nums3, nums4))

