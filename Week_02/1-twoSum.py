def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(1, lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j >= 0:
        return [j, i]
# 左右指针
# def twoSum(nums: List[int], target: int) -> List[int]:
#     temp = nums.copy()
#     temp.sort()
#     i = 0
#     j = len(nums) - 1
#     while i < j:
#         if (temp[i] + temp[j]) > target:
#             j = j - 1
#         elif (temp[i] + temp[j]) < target:
#             i = i + 1
#         else:
#             break
#     p = nums.index(temp[i])
#     nums.pop(p)  # 防止找到相同的temp[i],temp[j]
#     k = nums.index(temp[j])  # 找到在原数组的索引
#     if k >= p:  # 如果找到的k大于等于p,因为去掉了p,所以要给k加1
#         k = k + 1
#     return [p, k]
#
# #hash
#
# def twoSum(nums, target):
#     length = len(nums)
#     target_dict = {}
#     for i in range(length):
#         num = target - nums[i]
#         if num in target_dict:
#             return target_dict[num],i
#         target_dict[nums[i]] = i