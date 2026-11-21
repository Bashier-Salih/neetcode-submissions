class Solution:
    """
    UNDERSTAND:
    Input: array of ints
    Output: array of arrays
    Edge Cases: if no sums then return []

    Plan:
    result = []
    for i, num in enumerate(nums):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if (nums[l] + nums[r] + num) == 0:
                result.append([l, r, i])
            r -= 1
        while l < r:
            if (nums[l] + nums[r] + num) == 0:
                result.append([l, r, i])
            l += 1


    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + num
                if total == 0:
                    result.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result