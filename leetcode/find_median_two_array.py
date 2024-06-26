from typing import List
def find_median(nums1:List[int], nums2:List[int]) -> float:
    nums = sorted(nums1 + nums2)

    if len(nums) % 2 == 1:
        return nums[len(nums) // 2]
    return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

print(find_median([1,3], [2]))
print(find_median([1,4], [3,2]))