class Solution:
    """
    Understand:
    Input: a list of nums
    Output: the sum
    Edge cases: if num is length 1 -> return the index

    Plan:
    n = len(nums)
    if n == 1:
        return nums[0]
    
    final_max = float(-inf)
    current_sum = 0

    for r in range(n):
        if (current_sum += nums[r]) < final_max:
            current_sum = nums[r]
        else:
            current_sum += nums[r]
        final_max = max(final_max, current_sum)

        
        


    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        final_max = float("-inf")
        current_sum = 0

        for r in range(n):
            if (current_sum + nums[r]) < nums[r]:
                current_sum = nums[r]
            else:
                current_sum += nums[r]
            final_max = max(final_max, current_sum)
        return final_max
        