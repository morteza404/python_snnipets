from two_sum import two_sum

def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]