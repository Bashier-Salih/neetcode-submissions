class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        l, r = 0, len(nums) - 1
        while r > l:
            if nums[l] + nums[r] == target:
                return [l, r]
            elif (nums[l] + nums[r]) > target:
                r -= 1
            else:
                l -= 1
        return [-1,-1]