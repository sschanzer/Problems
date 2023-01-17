def findMedianSortedArrays(nums1: list, nums2: list) -> float:

        lst = []

        for i in nums1:
            lst.append(i)

        for j in nums2:
            lst.append(j)

        lst = sorted(lst)

        if len(lst) % 2 == 0:
            med_1 = lst[len(lst) // 2]
            med_2 = lst[len(lst) // 2 - 1]
            med = (med_1 + med_2) / 2
            return med
        else:
            med = lst[len(lst) // 2]
            return med

if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]))
    # 2.0
    print(findMedianSortedArrays([1,2], [3,4]))
    # 2.5