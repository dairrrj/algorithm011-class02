class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        else:
            last = nums[0]
            i=1
            while i != len(nums):
                if nums[i]==last:
                    nums.pop(i)
                    last = nums[i]
                    i+=1
            return len(nums)