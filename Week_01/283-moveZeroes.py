
def moveZeroes(self, nums: List[int]) -> None:
    j = 0
    for i, item in enumerate(nums):
        if item != 0:
            nums[j] = item
            if i != j:
                nums[i] = 0
            j += 1

# 直接交换的方法
# def moveZeroes(self, nums):
#     zero = 0
#     for i in xrange(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[zero] = nums[zero], nums[i]
#             zero += 1