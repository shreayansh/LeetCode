class Solution:
    def majorityElement(self, nums):
        nums = sorted(nums)
        i = 0
        for _ in range(len(set(nums))):
            if nums.count(nums[i]) >= len(nums) / 2:
                return nums[i]
            else:
                i = i + nums.count(nums[i])
