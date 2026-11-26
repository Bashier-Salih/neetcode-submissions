class Solution:
    """
    Understand:
    Input: an array of nums and an integer k
    Output: an array of the k most frequent element
    Edge cases: if len(nums) is less than or equal to 1 then just return num

    Plan:
    n = len(nums)
    freq = {}
    result = []
    count = [[]] * n

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for key, value in freq.items():
        count[value].append(key)
    print(count)

    
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        result = []
        count = [[] for i in range(n + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            count[value].append(key)
        
        for num in count[::-1]:
            for i in range(len(num)):
                result.append(num[i])
                if len(result) == k:
                    return result




        