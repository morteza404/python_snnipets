def has_trailing_zeros(nums):
    even_nums = 0
    for num in nums:
        even_nums += num % 2 == 0
    print(even_nums)
    return even_nums >= 2


def has_trailing_zeros_simple(nums):
    even_nums = 0
    for num in nums:
        if num % 2 == 0:
            even_nums += 1
    if even_nums >= 2:
        return True
    return False


nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 8, 16]
print(has_trailing_zeros(nums1))
print(has_trailing_zeros(nums2))
